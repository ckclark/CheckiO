from collections import defaultdict
def dfs(grid, x, y, r, c, g):
    if x == 9:
        yield grid
    elif y == 9:
        for ans in dfs(grid, x + 1, 0, r, c, g):
            yield ans
    else:
        if grid[x][y]:
            for ans in dfs(grid, x, y + 1, r, c, g):
                yield ans
        else:
            for i in xrange(1, 9 + 1):
                if i not in r[x] and i not in c[y] and i not in g[x / 3, y / 3]:
                    r[x].add(i)
                    c[y].add(i)
                    g[x / 3, y / 3].add(i)
                    grid[x][y] = i
                    for ans in dfs(grid, x, y + 1, r, c, g):
                        yield ans
                    grid[x][y] = 0
                    r[x].remove(i)
                    c[y].remove(i)
                    g[x / 3, y / 3].remove(i)

def checkio(grid):
    r = defaultdict(set)
    c = defaultdict(set)
    g = defaultdict(set)

    for i in xrange(9):
        for j in xrange(9):
            if grid[i][j]:
                v = grid[i][j]
                r[i].add(v)
                c[j].add(v)
                g[i / 3, j / 3].add(v)
    return next(dfs(grid, 0, 0, r, c, g))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([[0, 7, 1, 6, 8, 4, 0, 0, 0],
                    [0, 4, 9, 7, 0, 0, 0, 0, 0],
                    [5, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 8, 0, 0, 0, 0, 5, 0, 4],
                    [0, 0, 0, 3, 0, 7, 0, 0, 0],
                    [2, 0, 3, 0, 0, 0, 0, 9, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 9],
                    [0, 0, 0, 0, 0, 3, 7, 2, 0],
                    [0, 0, 0, 4, 9, 8, 6, 1, 0]]) == [[3, 7, 1, 6, 8, 4, 9, 5, 2],
                                                      [8, 4, 9, 7, 2, 5, 3, 6, 1],
                                                      [5, 6, 2, 9, 3, 1, 4, 7, 8],
                                                      [6, 8, 7, 2, 1, 9, 5, 3, 4],
                                                      [9, 1, 4, 3, 5, 7, 2, 8, 6],
                                                      [2, 5, 3, 8, 4, 6, 1, 9, 7],
                                                      [1, 3, 6, 5, 7, 2, 8, 4, 9],
                                                      [4, 9, 8, 1, 6, 3, 7, 2, 5],
                                                      [7, 2, 5, 4, 9, 8, 6, 1, 3]], "first"
    assert checkio([[5, 0, 0, 7, 1, 9, 0, 0, 4],
                    [0, 0, 1, 0, 3, 0, 5, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 8, 5, 9, 7, 2, 6, 4, 0],
                    [0, 0, 0, 6, 0, 1, 0, 0, 0],
                    [0, 2, 6, 3, 8, 5, 9, 1, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 3, 0, 5, 0, 2, 0, 0],
                    [8, 0, 0, 4, 9, 7, 0, 0, 6]]) == [[5, 6, 8, 7, 1, 9, 3, 2, 4],
                                                      [9, 7, 1, 2, 3, 4, 5, 6, 8],
                                                      [2, 3, 4, 5, 6, 8, 7, 9, 1],
                                                      [1, 8, 5, 9, 7, 2, 6, 4, 3],
                                                      [3, 9, 7, 6, 4, 1, 8, 5, 2],
                                                      [4, 2, 6, 3, 8, 5, 9, 1, 7],
                                                      [6, 1, 9, 8, 2, 3, 4, 7, 5],
                                                      [7, 4, 3, 1, 5, 6, 2, 8, 9],
                                                      [8, 5, 2, 4, 9, 7, 1, 3, 6]], "second"
    print('Local tests done')
