def checkio(number):
    L, U = 0, number
    while L + 1 < U:
        mid = L + (U - L) / 2
        if mid * (mid + 1) * (mid + 2) / 6 > number:
            U = mid
        else:
            L = mid
    return max(L * (L + 1) / 2, number - L * (L + 1) * (L + 2) / 6)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"
