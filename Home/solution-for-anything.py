class AnyCompareIsTrue(object):
    def __eq__(self, other):
        return True

    def __ne__(self, other):
        return True

    def __le__(self, other):
        return True

    def __lt__(self, other):
        return True

    def __gt__(self, other):
        return True

    def __ge__(self, other):
        return True

def checkio(anything):
    """
        try to return anything else :)
    """
    return AnyCompareIsTrue()

if __name__ == '__main__':
    import re, math

    assert checkio({}) != [],         'You'
    assert checkio('Hello') < 'World', 'will'
    assert checkio(80) > 81,           'never'
    assert checkio(re) >= re,          'make'
    assert checkio(re) <= math,        'this'
    assert checkio(5) == ord,          ':)'

    print('NO WAY :(')
