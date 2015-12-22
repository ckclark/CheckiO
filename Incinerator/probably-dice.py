def generating(coef, power):
    if power == 0:
        return [1]
    elif power % 2 == 0:
        tmp = generating(coef, power / 2)
        ans = [0] * (2 * len(tmp) - 1)
        for i1, v1 in enumerate(tmp):
            for i2, v2 in enumerate(tmp):
                ans[i1 + i2] += v1 * v2
        return ans
    else:
        tmp = generating(coef, power - 1)
        ans = [0] * (len(tmp) + len(coef) - 1)
        for i1, v1 in enumerate(tmp):
            for i2, v2 in enumerate(coef):
                ans[i1 + i2] += v1 * v2
        return ans

def probability(dice_number, sides, target):
    # generating function: https://en.wikipedia.org/wiki/Generating_function
    # the answer will be the coefficient of x^target in (x + x^2 + x^3 + ... + x^side) ^ dice_number
    try:
        return round(float(generating([0] + [1] * sides, dice_number)[target]) / (sides ** dice_number), 4)
    except IndexError:
        return 0.

if __name__ == '__main__':
    #These are only used for self-checking and are not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert(almost_equal(probability(2, 6, 3), 0.0556)), "Basic example"
    assert(almost_equal(probability(2, 6, 4), 0.0833)), "More points"
    assert(almost_equal(probability(2, 6, 7), 0.1667)), "Maximum for two 6-sided dice"
    assert(almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
    assert(almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
    assert(almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
    assert(almost_equal(probability(10, 10, 50), 0.0375)), "Many dice, many sides"
