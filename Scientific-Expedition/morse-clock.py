def checkio(time_string):
    h, m, s = map(int, time_string.split(':'))
    return '{:02b} {:04b} : {:03b} {:04b} : {:03b} {:04b}'.format(h / 10, h % 10, m / 10, m % 10, s / 10, s % 10).replace('0', '.').replace('1', '-')

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u"10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio(u"21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio(u"00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio(u"23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"

