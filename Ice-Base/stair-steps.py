def checkio(numbers):
    numbers = [0] + numbers + [0]
    for i in xrange(1, len(numbers)):
        ans = numbers[i - 1]
        if i >= 2:
            ans = max(ans, numbers[i - 2])
        numbers[i] += ans
    return numbers[-1]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([5, -3, -1, 2]) == 6, 'Fifth'
    assert checkio([5, 6, -10, -7, 4]) == 8, 'First'
    assert checkio([-11, 69, 77, -51, 23, 67, 35, 27, -25, 95]) == 393, 'Second'
    assert checkio([-21, -23, -69, -67, 1, 41, 97, 49, 27]) == 125, 'Third'
    print('All ok')
