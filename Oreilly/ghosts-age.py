def get_fib():
    fib = []
    a, b = 1, 2
    while a <= 10000:
        fib.append(a)
        a, b = b, a + b
    return fib

def checkio(opacity):
    if opacity == 10000: return 0
    fib = get_fib()
    for i, v in enumerate(fib[1:]):
        if v + i > 10000 - opacity:
            idx = i
            break
    return opacity - (10000 - v - idx) + fib[idx] - 1

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"
