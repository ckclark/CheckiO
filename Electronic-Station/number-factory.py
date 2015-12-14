def checkio(number):
    usage = [0] * 10
    for n in xrange(9, 1, -1):
        while number > 0 and number % n == 0:
            number /= n
            usage[n] += 1
    if number > 1:
        return 0
    else:
        return int(''.join(str(x) * usage[x] for x in xrange(10)))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(3125) == 55555, "5th example"
    assert checkio(9973) == 0, "6th example"
