def convert(numerator, denominator):
    remainder = dict()
    ans = []
    ans.append(str(numerator / denominator))
    ans.append('.')
    numerator %= denominator
    if numerator:
        idx = 0
        decimal = []
        while numerator:
            numerator *= 10
            pos = remainder.setdefault(numerator, idx)
            if pos == idx:
                decimal.append(str(numerator / denominator))
                numerator %= denominator
                idx += 1
            else:
                ans.extend(decimal[:pos])
                ans.append('(')
                ans.extend(decimal[pos:])
                ans.append(')')
                break
        else:
            ans.extend(decimal)
    return ''.join(ans)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert convert(1, 3) == "0.(3)", "1/3 Classic"
    assert convert(5, 3) == "1.(6)", "5/3 The same, but bigger"
    assert convert(3, 8) == "0.375", "3/8 without repeating part"
    assert convert(7, 11) == "0.(63)", "7/11 prime/prime"
    assert convert(29, 12) == "2.41(6)", "29/12 not and repeating part"
    assert convert(11, 7) == "1.(571428)", "11/7 six digits"
    assert convert(0, 117) == "0.", "Zero"
