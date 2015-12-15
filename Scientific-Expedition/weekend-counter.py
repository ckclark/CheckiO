from datetime import date, timedelta


def checkio(from_date, to_date):
    diff_days = ((to_date - from_date).days + 1)
    ans = diff_days / 7 * 2
    for i in xrange(diff_days % 7):
        if (from_date + timedelta(days=i)).weekday() in (5, 6):
            ans += 1
    return ans

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2, "1st example"
    assert checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8, "2nd example"
    assert checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2, "3rd example"

