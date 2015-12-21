from fractions import Fraction

def divide_pie(groups):
    total = sum(map(abs, groups))
    remaining = Fraction(1)
    for group in groups:
        if group > 0:
            remaining -= Fraction(group, total)
        else:
            remaining *= Fraction(total + group, total)
    return (remaining.numerator, remaining.denominator)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance((2, -2), (tuple, list)), "Return tuple or list"
    assert tuple(divide_pie((2, -1, 3))) == (1, 18), "Example"
    assert tuple(divide_pie((1, 2, 3))) == (0, 1), "All know about the pie"
    assert tuple(divide_pie((-1, -1, -1))) == (8, 27), "One by one"
    assert tuple(divide_pie((10,))) == (0, 1), "All together"
