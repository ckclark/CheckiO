def det(a, b, c, d):
    return a * d - b * c

def shot(wall1, wall2, shot_point, later_point):
    vwx = wall2[0] - wall1[0]
    vwy = wall2[1] - wall1[1]
    pw = wall1

    vsx = later_point[0] - shot_point[0]
    vsy = later_point[1] - shot_point[1]
    ps = shot_point

    den = det(vsx, -vwx, vsy, -vwy)
    numt = det(pw[0] - ps[0], -vwx, pw[1] - ps[1], -vwy)
    nums = det(vsx, pw[0] - ps[0], vsy, pw[1] - ps[1])
    if den == 0:
        return -1
    t = float(numt) / den
    s = float(nums) / den
    if t > 0 and -1e-5 < s < 1 + 1e-5:
        return int((.5 - abs(s - .5)) * 200 + .5)
    return -1

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert shot((2, 2), (5, 7), (11, 2), (8, 3)) == 100, "1st case"
    assert shot((2, 2), (5, 7), (11, 2), (7, 2)) == 0, "2nd case"
    assert shot((2, 2), (5, 7), (11, 2), (8, 4)) == 29, "3th case"
    assert shot((2, 2), (5, 7), (11, 2), (9, 5)) == -1, "4th case"
    assert shot((2, 2), (5, 7), (11, 2), (10.5, 3)) == -1, "4th case again"
