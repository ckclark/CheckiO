import datetime
def most_frequent_days(year):
    """
        List of most frequent days of the week in the given year
    """
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    is_leap = year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)
    first_weekday = datetime.date(year, 1, 1).weekday()
    ans = [first_weekday]
    if is_leap:
        ans.append((first_weekday + 1) % 7)
    ans.sort()
    ans = map(weekdays.__getitem__, ans)
    return ans

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent_days(2399) ==  ['Friday'], "1st example"
    assert most_frequent_days(1152) == ['Tuesday', 'Wednesday'], "2nd example"
    assert most_frequent_days(56) == ['Saturday', 'Sunday'], "3rd example"
    assert most_frequent_days(2909) == ['Tuesday'], "4th example"
