from collections import defaultdict
from fractions import Fraction
from operator import add, sub, mul
from itertools import product

def checkio(data):
    dp = defaultdict(set)
    digits = len(data) # should be 6
    ops = {add, sub, mul}
    for i in xrange(digits):
        for j in xrange(i + 1, digits + 1):
            dp[i, j - i].add(Fraction(data[i:j]))

    for l in xrange(2, digits + 1):
        for i in xrange(0, digits - l + 1):
            for j in xrange(i + 1, i + l):
                dp[i, l].update([op(x, y) for op in ops for (x, y) in product(dp[i, j - i], dp[j, i + l - j])])
                dp[i, l].update([x / y for (x, y) in product(dp[i, j - i], dp[j, i + l - j]) if y != 0])
    return 100 not in dp[0, digits]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u'000000') == True, "All zeros"
    assert checkio(u'707409') == True, "You can not transform it to 100"
    assert checkio(u'595347') == False, "(5 + ((9 / (3 / 34)) - 7)) = 100"
    assert checkio(u'271353') == False, "(2 - (7 * (((1 / 3) - 5) * 3))) = 100"
