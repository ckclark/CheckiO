from collections import defaultdict
def checkio(matrix):
    w, h = len(matrix[0]), len(matrix)
    d = {
        1: (0, 1),
        2: (1, -1),
        4: (1, 0),
        8: (1, 1),
    }
    tried = defaultdict(int)
    for i in xrange(h):
        for j in xrange(w):
            c = matrix[i][j]
            for k, v in d.iteritems():
                if tried[i, j] & k == 0:
                    tried[i, j] |= k
                    for l in xrange(1, 4):
                        np = (i + v[0] * l, j + v[1] * l)
                        if 0 <= np[0] < h and 0 <= np[1] < w:
                            if matrix[np[0]][np[1]] != c:
                                break
                            tried[np[0], np[1]] |= k
                        else:
                            break
                    else:
                        return True
    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
