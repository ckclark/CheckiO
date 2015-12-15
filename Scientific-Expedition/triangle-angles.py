from math import acos, pi

def checkio(a, b, c):
    if a + b <= c or abs(a - b) >= c:
        return [0, 0, 0]
    angles = []
    angles.append(int(acos(float(a * a + b * b - c * c) / (2 * a * b)) / pi * 180 + .5))
    angles.append(int(acos(float(a * a + c * c - b * b) / (2 * a * c)) / pi * 180 + .5))
    angles.append(int(acos(float(c * c + b * b - a * a) / (2 * c * b)) / pi * 180 + .5))
    angles.sort()
    return angles

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
