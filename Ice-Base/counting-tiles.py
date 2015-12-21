def checkio(radius):
    solid = 0
    cover = 0
    for x in xrange(1, 4):
        for y in xrange(1, 4):
            if x * x + y * y + 1e-5 < radius * radius:
                solid += 1
    for x in xrange(4):
        for y in xrange(4):
            if x * x + y * y + 1e-5 < radius * radius:
                cover += 1
    return [solid * 4, (cover - solid) * 4]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(2) == [4, 12], "N=2"
    assert checkio(3) == [16, 20], "N=3"
    assert checkio(2.1) == [4, 20], "N=2.1"
    assert checkio(2.5) == [12, 20], "N=2.5"
