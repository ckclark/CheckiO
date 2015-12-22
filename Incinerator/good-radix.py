def checkio(number):
    for i in xrange(2, 36 + 1):
        try:
            if int(number, i) % (i - 1) == 0:
                return i
        except ValueError:
            pass
    return 0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u"18") == 10, "Simple decimal"
    assert checkio(u"1010101011") == 2, "Any number is divisible by 1"
    assert checkio(u"222") == 3, "3rd test"
    assert checkio(u"A23B") == 14, "It's not a hex"
    assert checkio(u"IDDQD") == 0, "k is not exist"
    print('Local tests done')
