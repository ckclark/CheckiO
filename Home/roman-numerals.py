def checkio(data):
    thousand = ["", "M", "MM", "MMM"]
    hundred  = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    ten      = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    one      = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    ans = []

    ans.append(one[data % 10])
    data /= 10
    ans.append(ten[data % 10])
    data /= 10
    ans.append(hundred[data % 10])
    data /= 10
    ans.append(thousand[data % 10])
    return ''.join(reversed(ans))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
