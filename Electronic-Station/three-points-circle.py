import re
def det(a1, b1, a2, b2):
    return a1 * b2 - a2 * b1

def checkio(data):

    points = []
    for p in re.compile(r'\([0-9.]+,[0-9.]+\)').findall(data):
        mat = re.match(r'\(([0-9.]+),([0-9.]+)\)', p)
        points.append((float(mat.group(1)), float(mat.group(2))))
    mid1 = ((points[0][0] + points[1][0]) / 2, (points[0][1] + points[1][1]) / 2)
    mid2 = ((points[0][0] + points[2][0]) / 2, (points[0][1] + points[2][1]) / 2)
    u1 = points[1][1] - points[0][1]
    v1 = points[0][0] - points[1][0]

    u2 = points[2][1] - points[0][1]
    v2 = points[0][0] - points[2][0]

    t = det(mid2[1] - mid1[1], -v2, mid2[0] - mid1[0], -u2) / det(v1, -v2, u1, -u2)
    c = (mid1[0] + t * u1, mid1[1] + t * v1)
    r = ((points[0][0] - c[0]) ** 2 + (points[0][1] - c[1]) ** 2) ** .5
    formatted = lambda x: format(x, '+.2f').rstrip('0').rstrip('.')
    formatted2 = lambda x: format(x, '.2f').rstrip('0').rstrip('.')
    return "(x%s)^2+(y%s)^2=%s^2" % (formatted(-c[0]), formatted(-c[1]), formatted2(r))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio(u"(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"
