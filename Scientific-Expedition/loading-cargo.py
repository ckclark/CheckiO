def checkio(data):
    s = sum(data)
    dp = [False] * (s + 1)
    dp[0] = True
    for v in data:
        for i in xrange(s, v - 1, -1):
            if dp[i - v]:
                dp[i] = True
    return min(abs(s - 2 * i) for i, v in enumerate(dp) if v)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([10, 10]) == 0, "1st example"
    assert checkio([10]) == 10, "2nd example"
    assert checkio([5, 8, 13, 27, 14]) == 3, "3rd example"
    assert checkio([5, 5, 6, 5]) == 1, "4th example"
    assert checkio([12, 30, 30, 32, 42, 49]) == 9, "5th example"
    assert checkio([1, 1, 1, 3]) == 0, "6th example"
