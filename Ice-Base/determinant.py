from itertools import cycle
def checkio(data):
    size = len(data)
    if size == 1:
        return data[0][0]
    ans = 0
    for sign, (col, n) in zip(cycle((1, -1)), enumerate(data[0])):
        submatrix = [[v for y, v in enumerate(data[x]) if y != col] for x in xrange(1, size) ]
        ans += sign * n * checkio(submatrix)
    return ans

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[4, 3], [6, 3]]) == -6, 'First example'

    assert checkio([[1, 3, 2],
                    [1, 1, 4],
                    [2, 2, 1]]) == 14, 'Second example'
