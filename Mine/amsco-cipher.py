def decode_amsco(message, key):
    message = filter(lambda x:x.isalpha(), message)
    charcnt = len(message)
    key = str(key)
    keylength = len(key)
    n = charcnt
    grid = []
    rowcnt = 0
    while n > 0:
        row = []
        grid.append(row)
        for i in xrange(keylength):
            v = min((i + rowcnt) % 2 + 1, n)
            row.append(v)
            n -= v
        rowcnt += 1
    it = iter(message)
    for _, col in sorted(zip(key, xrange(keylength))):
        for r in xrange(rowcnt):
            grid[r][col] = ''.join(next(it) for _ in xrange(grid[r][col]))
    return ''.join(map(''.join, grid))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert decode_amsco(u"oruoreemdstmioitlpslam", 4123) == "loremipsumdolorsitamet", "Lorem Ipsum"
    assert decode_amsco(u'kicheco', 23415) == "checkio", "Checkio"
    assert decode_amsco(u'hrewhoorrowyilmmmoaouletow', 123) == "howareyouwillhometommorrow", "How are you"
