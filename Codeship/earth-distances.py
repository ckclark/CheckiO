# -*- coding:utf8 -*-
from math import sin, cos, acos, pi
import re
R = 6371

def distance(first, second):
    latdeg1, latmin1, latsec1, latori1, longdeg1, longmin1, longsec1, longori1 = filter(None, re.split(ur'[°′″, ]', first))
    latdeg2, latmin2, latsec2, latori2, longdeg2, longmin2, longsec2, longori2 = filter(None, re.split(ur'[°′″, ]', second))
    lat1 = (float(latdeg1) + float(latmin1) / 60 + float(latsec1) / 3600) * (1 if latori1.startswith('N') else -1) * pi / 180
    long1 = (float(longdeg1) + float(longmin1) / 60 + float(longsec1) / 3600) * (1 if longori1 == 'E' else -1) * pi / 180
    lat2 = (float(latdeg2) + float(latmin2) / 60 + float(latsec2) / 3600) * (1 if latori2.startswith('N') else -1) * pi / 180
    long2 = (float(longdeg2) + float(longmin2) / 60 + float(longsec2) / 3600) * (1 if longori2 == 'E' else -1) * pi / 180
    x1, y1, z1 = cos(lat1) * sin(long1), cos(lat1) * cos(long1), sin(lat1)
    x2, y2, z2 = cos(lat2) * sin(long2), cos(lat2) * cos(long2), sin(lat2)
    cross_d = ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** .5
    theta = acos(1 - cross_d ** 2 / 2)
    return R * theta


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=1):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(
        distance(u"51°28′48″N 0°0′0″E", u"46°12′0″N, 6°9′0″E"), 739.2), "From Greenwich to Geneva"
    assert almost_equal(
        distance(u"90°0′0″N 0°0′0″E", u"90°0′0″S, 0°0′0″W"), 20015.1), "From South to North"
    assert almost_equal(
        distance(u"33°51′31″S, 151°12′51″E", u"40°46′22″N 73°59′3″W"), 15990.2), "Opera Night"
