def checkio(required, operations):
    for step in xrange(1, len(operations) + 1):
        points = sorted(sum([[(op[0], 1), (op[1] + 1, -1)] for op in operations[:step]], []))
        prev = points[0][0]
        level = 0
        painted = 0
        for p in points:
            if level > 0:
                painted += p[0] - prev
            level += p[1]
            prev = p[0]
        if painted >= required:
            return step
    return -1

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(5, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 1, "1st"
    assert checkio(6, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 2, "2nd"
    assert checkio(11, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 3, "3rd"
    assert checkio(16, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 4, "4th"
    assert checkio(21, [[1, 5], [11, 15], [2, 14], [21, 25]]) == -1, "not enough"
    assert checkio(1000000011, [[1, 1000000000], [11, 1000000010]]) == -1, "large"
