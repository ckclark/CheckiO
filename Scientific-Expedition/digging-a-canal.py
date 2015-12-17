import heapq

class Node(object):
    def __init__(self, idx, dis):
        self.idx = idx
        self.dis = dis

    def __lt__(self, other):
        return self.dis < other.dis


def checkio(land_map):
    w, h = len(land_map[0]), len(land_map)

    dijkstra = [Node((0, i), land_map[0][i]) for i in xrange(w)]
    heapq.heapify(dijkstra)

    visited = set()

    while True:
        cur = heapq.heappop(dijkstra)
        if cur.idx[0] == h - 1:
            return cur.dis
        if cur.idx not in visited:
            visited.add(cur.idx)
            for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                nx, ny = cur.idx[0] + dx, cur.idx[1] + dy
                if 0 <= nx < h and 0 <= ny < w:
                    md = cur.dis + land_map[nx][ny]
                    heapq.heappush(dijkstra, Node((nx, ny), md))
    return 'Not gonna happen'

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[1, 1, 1, 1, 0, 1, 1],
                    [1, 1, 1, 1, 0, 0, 1],
                    [1, 1, 1, 1, 1, 0, 1],
                    [1, 1, 0, 1, 1, 0, 1],
                    [1, 1, 0, 1, 1, 1, 1],
                    [1, 0, 0, 1, 1, 1, 1],
                    [1, 0, 1, 1, 1, 1, 1]]) == 2, "1st example"
    assert checkio([[0, 0, 0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 0, 1, 0, 1, 1],
                    [1, 0, 0, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0, 0, 0]]) == 3, "2nd example"
    assert checkio([[1, 1, 1, 1, 1, 0, 1, 1],
                    [1, 0, 1, 1, 1, 0, 1, 1],
                    [1, 0, 1, 0, 1, 0, 1, 0],
                    [1, 0, 1, 1, 1, 0, 1, 1],
                    [0, 0, 1, 1, 0, 0, 0, 0],
                    [1, 0, 1, 1, 1, 1, 1, 1],
                    [1, 0, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 0, 1, 1, 1, 1]]) == 2, "3rd example"
