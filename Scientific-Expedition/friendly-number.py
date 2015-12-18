def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    answer = []
    prefix = '-' if number < 0 else ''
    answer.append(prefix)
    number = abs(number)
    answer.append('') # placeholder
    for p in powers:
        if decimals == 0:
            answer[-1] = '{number}{power}'.format(number=number, power=p)
            if number < base:
                break
            number /= base
        else:
            answer[-1] = '{number:.0{width}f}{power}'.format(number=number, width=decimals, power=p)
            if number < base:
                break
            number = float(number) / base


    answer.append(suffix)
    return ''.join(answer)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert friendly_number(102) == '102', '102'
    assert friendly_number(10240) == '10k', '10k'
    assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
    assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
    assert friendly_number(1024000000, base=1024, suffix='iB') == '976MiB', '976MiB'
