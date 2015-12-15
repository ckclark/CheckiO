def check_square(lines_set, p, l):
    for i in xrange(l):
        if (p + i, p + (i + 1)) not in lines_set:
            return False
    for i in xrange(l):
        if (p + i * 4, p + (i + 1) * 4) not in lines_set:
            return False
    for i in xrange(l):
        if ((p + l * 4) + i, (p + l * 4) + (i + 1)) not in lines_set:
            return False
    for i in xrange(l):
        if ((p + l) + i * 4, (p + l) + (i + 1) * 4) not in lines_set:
            return False
    return True

def checkio(lines_list):
    lines_set = set(map(lambda x:tuple(sorted(x)), lines_list))
    ans = 0
    for i in xrange(1, 16 + 1):
        for l in xrange(1, (4 - (i % 4)) % 4 + 1):
            if check_square(lines_set, i, l):
                ans += 1
    return ans


if __name__ == '__main__':
    assert (checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
                     [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
                     [10, 14], [12, 16], [14, 15], [15, 16]]) == 3), "First, from description"
    assert (checkio([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
                     [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
                     [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16]]) == 2), "Second, from description"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 6]]) == 1), "Third, one small square"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 9], [6, 10], [9, 10]]) == 0), "Fourth, it's not square"
    assert (checkio([[16, 15], [16, 12], [15, 11], [11, 10],
                     [10, 14], [14, 13], [13, 9]]) == 0), "Fifth, snake"
