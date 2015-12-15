import heapq
from collections import defaultdict

class Max(object):
    def __gt__(self, other):
        return True

class Node(object):
    def __init__(self, idx):
        self.idx = idx
        self.dis = Max()

    def __lt__(self, other):
        return self.dis < other.dis

def capture(matrix):
    n = len(matrix)
    dis = dict()
    adj_list = defaultdict(list)
    for i in xrange(n):
        for j in xrange(i):
            if matrix[i][j]:
                dis[i, j] = matrix[j][j]
                dis[j, i] = matrix[i][i]
                adj_list[i].append(j)
                adj_list[j].append(i)
    nodes = map(Node, xrange(n))
    nodes[0].dis = 0
    dijkstra = nodes[:]
    visited = set()
    max_dis = 0
    while dijkstra:
        cur = heapq.heappop(dijkstra)
        if cur.idx not in visited:
            max_dis = cur.dis
            visited.add(cur.idx)
            for adj in adj_list[cur.idx]:
                if nodes[adj].dis > cur.dis + dis[cur.idx, adj]:
                    nodes[adj] = newnode = Node(adj)
                    newnode.dis = cur.dis + dis[cur.idx, adj]
                    heapq.heappush(dijkstra, newnode)
    return max_dis

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 8, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 8, "Base example"
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 1, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 4, "Low security"
    assert capture([[0, 1, 1],
                    [1, 9, 1],
                    [1, 1, 9]]) == 9, "Small"
