import heapq
def checkio(field_map):
    w, h = len(field_map[0]), len(field_map)
    for i in xrange(h):
        for j in xrange(w):
            if field_map[i][j] == 'S':
                start = i, j
            elif field_map[i][j] == 'E':
                end = i, j
    LOADED = 2
    #UNLOADED = 1
    OTHER = lambda x:3 - x
    dijkstra = []
    dijkstra.append((0, start, LOADED))
    shortestdis = dict()
    prev = dict()
    while dijkstra:
        dis, pos, state = heapq.heappop(dijkstra)
        if (pos, state) == (end, LOADED):
            ans = []
            while (pos, state) != (start, LOADED):
                (pos, state), c = prev[pos, state]
                ans.append(c)
            return ''.join(ans)[::-1]
        else:
            for d, c in [([-1, 0], 'U'), ([1, 0], 'D'), ([0, -1], 'L'), ([0, 1], 'R')]:
                nx, ny = pos[0] + d[0], pos[1] + d[1]
                if 0 <= nx < h and 0 <= ny < w and field_map[nx][ny] != 'W':
                    ndis = dis + state
                    tdis = shortestdis.get(((nx, ny), state))
                    if tdis is None or tdis > ndis:
                        heapq.heappush(dijkstra, (ndis, (nx, ny), state))
                        shortestdis[(nx, ny), state] = ndis
                        prev[(nx, ny), state] = ((pos, state), c)

                    if field_map[nx][ny] == 'B':
                        ndis = dis + state + 1
                        tdis = shortestdis.get(((nx, ny), OTHER(state)))
                        if tdis is None or tdis > ndis:
                            heapq.heappush(dijkstra, (ndis, (nx, ny), OTHER(state)))
                            shortestdis[(nx, ny), OTHER(state)] = ndis
                            prev[(nx, ny), OTHER(state)] = ((pos, state), 'B' + c)

if __name__ == '__main__':
    #This part is using only for self-checking and not necessary for auto-testing
    ACTIONS = {
        "L": (0, -1),
        "R": (0, 1),
        "U": (-1, 0),
        "D": (1, 0),
        "B": (0, 0)
    }

    def check_solution(func, max_time, field):
        max_row, max_col = len(field), len(field[0])
        s_row, s_col = 0, 0
        total_time = 0
        hold_box = True
        route = func(field[:])
        for step in route:
            if step not in ACTIONS:
                print("Unknown action {0}".format(step))
                return False
            if step == "B":
                if hold_box:
                    if field[s_row][s_col] == "B":
                        hold_box = False
                        total_time += 1
                        continue
                    else:
                        print("Stephan broke the cargo")
                        return False
                else:
                    if field[s_row][s_col] == "B":
                        hold_box = True
                    total_time += 1
                    continue
            n_row, n_col = s_row + ACTIONS[step][0], s_col + ACTIONS[step][1],
            total_time += 2 if hold_box else 1
            if 0 > n_row or n_row >= max_row or 0 > n_col or n_row >= max_col:
                print("We've lost Stephan.")
                return False
            if field[n_row][n_col] == "W":
                print("Stephan fell in water.")
                return False
            s_row, s_col = n_row, n_col
            if field[s_row][s_col] == "E" and hold_box:
                if total_time <= max_time:
                    return True
                else:
                    print("You can deliver the cargo faster.")
                    return False
        print("The cargo is not delivered")
        return False

    assert check_solution(checkio, 12, ["S...", "....", "B.WB", "..WE"]), "1st Example"
    assert check_solution(checkio, 11, ["S...", "....", "B..B", "..WE"]), "2nd example"
    assert check_solution(checkio, 13, ["SBBBBB","BBBBBB","BBBBBB","BBBBBB","BBBBBE"]), "should be 13"
