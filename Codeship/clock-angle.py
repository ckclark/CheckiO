def clock_angle(time):
    h, m = map(int, time.split(':'))
    h %= 12
    h = (h + m / 60.) * 30
    m *= 6
    angle = abs(h - m)
    if angle > 180:
        angle = 360 - angle
    return round(angle, 1)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert clock_angle("02:30") == 105, "02:30"
    assert clock_angle("13:42") == 159, "13:42"
    assert clock_angle("01:42") == 159, "01:42"
    assert clock_angle("01:43") == 153.5, "01:43"
    assert clock_angle("00:00") == 0, "Zero"
    assert clock_angle("12:01") == 5.5, "Little later"
    assert clock_angle("18:00") == 180, "Opposite"
