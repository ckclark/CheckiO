from collections import defaultdict

def dfs(adj_list, cur, visited, curans):
    global ans
    if curans[0] in adj_list[cur] and len(curans) + 1 > max(3, len(ans)):
        ans = curans + [curans[0]]
    for nxt in adj_list[cur]:
        if nxt not in visited:
            curans.append(nxt)
            visited.add(nxt)
            dfs(adj_list, nxt, visited, curans)
            visited.remove(nxt)
            curans.pop()

def find_cycle(connections):
    global ans
    nodes = list(reduce(set.union, connections, set()))
    adj_list = defaultdict(set)
    for a, b in connections:
        adj_list[a].add(b)
        adj_list[b].add(a)

    ans = []
    for start in nodes:
        dfs(adj_list, start, set([start]), [start])
    return ans

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def checker(function, connections, best_size):
        user_result = function(connections)
        if not isinstance(user_result, (tuple, list)) or not all(isinstance(n, int) for n in user_result):
            print("You should return a list/tuple of integers.")
            return False
        if not best_size and user_result:
            print("Where did you find a cycle here?")
            return False
        if not best_size and not user_result:
            return True
        if len(user_result) < best_size + 1:
            print("You can find a better loop.")
            return False
        if user_result[0] != user_result[-1]:
            print("A cycle starts and ends in the same node.")
            return False
        if len(set(user_result)) != len(user_result) - 1:
            print("Repeat! Yellow card!")
            return False
        for n1, n2 in zip(user_result[:-1], user_result[1:]):
            if (n1, n2) not in connections and (n2, n1) not in connections:
                print("{}-{} is not exist".format(n1, n2))
                return False
        return True, "Ok"

    assert checker(find_cycle,
                   ((1, 2), (2, 3), (3, 4), (4, 5), (5, 7), (7, 6),
                    (8, 5), (8, 4), (1, 5), (2, 4), (1, 8)), 6), "Example"
    assert checker(find_cycle,
                   ((1, 2), (2, 3), (3, 4), (4, 5), (5, 7), (7, 6), (8, 4), (1, 5), (2, 4)), 5), "Second"
