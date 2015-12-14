def link_parent(parent, pa, pb):
    parent[pa][0] = pb
    parent[pb][1] += parent[pa][1]

def find_root(parent, p): # p: (x, y)
    if parent[p][0] != p: # parent[p]: [(x', y'), size]
        parent[p] = find_root(parent, parent[p][0])
    return parent[p]

def checkio(matrix):
    parent = dict()
    w, h = len(matrix[0]), len(matrix)
    for i in xrange(h):
        for j in xrange(w):
            parent[i, j] = [(i, j), 1]
    for x in xrange(h):
        for y in xrange(w):
            for d in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nx, ny = x + d[0], y + d[1]
                if 0 <= nx < h and 0 <= ny < w:
                    if matrix[x][y] == matrix[nx][ny]:
                        pa = find_root(parent, (x, y))
                        pb = find_root(parent, (nx, ny))
                        if pa[0] != pb[0]:
                            link_parent(parent, pa[0], pb[0])
    v = max(parent, key=lambda x:parent[x][1])
    return [parent[v][1], matrix[v[0]][v[1]]]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        [1, 2, 3, 4, 5],
        [1, 1, 1, 2, 3],
        [1, 1, 1, 2, 2],
        [1, 2, 2, 2, 1],
        [1, 1, 1, 1, 1]
    ]) == [14, 1], "14 of 1"

    assert checkio([
        [2, 1, 2, 2, 2, 4],
        [2, 5, 2, 2, 2, 2],
        [2, 5, 4, 2, 2, 2],
        [2, 5, 2, 2, 4, 2],
        [2, 4, 2, 2, 2, 2],
        [2, 2, 4, 4, 2, 2]
    ]) == [19, 2], '19 of 2'
