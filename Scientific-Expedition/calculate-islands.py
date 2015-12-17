def link_parent(parent, ra, rb):
    if ra[1] > rb[1]:
        parent[rb[0]] = ra
        ra[1] += rb[1]
    else:
        parent[ra[0]] = rb
        rb[1] += ra[1]

def find_root(parent, n):
    if parent[n][0] != n:
        parent[n] = find_root(parent, parent[n][0])
    return parent[n]

def checkio(land_map):

    parent = dict()
    w, h = len(land_map[0]), len(land_map)
    for i in xrange(h):
        for j in xrange(w):
            if land_map[i][j]:
                parent[i, j] = [(i, j), 1]

    for i in xrange(h):
        for j in xrange(w):
            if land_map[i][j]:
                for d in [(-1, 0), (0, -1), (-1, 1), (-1, -1)]:
                    nx, ny = i + d[0], j + d[1]
                    if 0 <= nx < h and 0 <= ny < w and land_map[nx][ny]:
                        ra = find_root(parent, (i, j))
                        rb = find_root(parent, (nx, ny))
                        if ra != rb:
                            link_parent(parent, ra, rb)

    visited = set()
    sizes = []
    for i in xrange(h):
        for j in xrange(w):
            if land_map[i][j]:
                r = find_root(parent, (i, j))
                if r[0] not in visited:
                    visited.add(r[0])
                    sizes.append(r[1])
    return sorted(sizes)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0]]) == [1, 3], "1st example"
    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 1, 0, 0]]) == [5], "2nd example"
    assert checkio([[0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 1, 1, 1],
                    [1, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0]]) == [2, 3, 3, 4], "3rd example"
