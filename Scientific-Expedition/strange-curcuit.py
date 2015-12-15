from operator import sub
def find_pos(n):
    print 'n:', n
    near_sqrt = int((n + .5) ** .5)
    if near_sqrt % 2 == 0:
        pos = [near_sqrt / 2, - (near_sqrt / 2) + 1]
        rem = n - near_sqrt * near_sqrt

        move = min(rem, 1)
        pos[1] -= move
        rem -= move

        move = min(rem, near_sqrt)
        pos[0] -= move
        rem -= move

        pos[1] += rem
    else:
        pos = [-(near_sqrt / 2), near_sqrt / 2]
        rem = n - near_sqrt * near_sqrt

        move = min(rem, 1)
        pos[1] += move
        rem -= move

        move = min(rem, near_sqrt)
        pos[0] += move
        rem -= move

        pos[1] -= rem
    return pos


def find_distance(first, second):
    first = find_pos(first)
    second = find_pos(second)
    return sum(map(abs, map(sub, first, second)))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_distance(1, 9) == 2, "First"
    assert find_distance(9, 1) == 2, "Reverse First"
    assert find_distance(10, 25) == 1, "Neighbours"
    assert find_distance(5, 9) == 4, "Diagonal"
    assert find_distance(26, 31) == 5, "One row"
    assert find_distance(50, 16) == 10, "One more test"
