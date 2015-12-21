def map_point(c):
    v = (ord(c) - 48) * 2
    if v >= 10:
        v = v / 10 + v % 10
    return v

def checkio(data):
    data = filter(lambda x:x.isalnum(), data)
    s = sum(map(map_point, data[-1::-2])) + sum(map(lambda x:ord(x) - 48, data[-2::-2]))
    return [chr(48 + (10 - s % 10) % 10), s]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert (checkio(u"799 273 9871") == ["3", 67]), "First Test"
    assert (checkio(u"139-MT") == ["8", 52]), "Second Test"
    assert (checkio(u"123") == ["0", 10]), "Test for zero"
    assert (checkio(u"999_999") == ["6", 54]), "Third Test"
    assert (checkio(u"+61 820 9231 55") == ["3", 37]), "Fourth Test"
    assert (checkio(u"VQ/WEWF/NY/8U") == ["9", 201]), "Fifth Test"

    print("OK, done!")
