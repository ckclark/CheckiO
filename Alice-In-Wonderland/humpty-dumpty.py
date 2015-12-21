from math import pi, asin, atanh
def checkio(height, width):
    if height > width: # prolate
        c, a = float(height) / 2, float(width) / 2
        e = (1 - a * a / c / c) ** .5
        v, s = c * a * a * 4. / 3 * pi, 2 * pi * a * a * (1 + c / a / e * asin(e))
    elif height < width:
        c, a = float(height) / 2, float(width) / 2
        e = (1 - c * c / a / a) ** .5
        v, s = c * a * a * 4. / 3 * pi, 2 * pi * a * a * (1 + (1 - e * e) / e * atanh(e))
    else:
        c, a = float(height) / 2, float(width) / 2
        v, s = c * c * c * 4 / 3 * pi, 4 * pi * c * c
    return [round(v, 2), round(s, 2)]


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 2) == [8.38, 21.48], "Prolate spheroid"
    assert checkio(2, 2) == [4.19, 12.57], "Sphere"
    assert checkio(2, 4) == [16.76, 34.69], "Oblate spheroid"
