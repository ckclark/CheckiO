def checkio(previous):
    test = [[0, 0], [9, 0], [0, 9]]
    if len(previous) < 3:
        return test[len(previous)]
    for i in xrange(10):
        for j in xrange(10):
            for x, y, d in previous:
                if int(((x - i) * (x - i) + (y - j) * (y - j)) ** .5 + .5) != d:
                    break
            else:
                return (i, j)
    return 'Give up'

if __name__ == '__main__':
    #This part is using only for self-testing.
    def check_solution(func, ore):
        recent_data = []
        for step in range(4):
            row, col = func([d[:] for d in recent_data])  # copy the list
            if row < 0 or row > 9 or col < 0 or col > 9:
                print("Where is our probe?")
                return False
            if (row, col) == ore:
                return True
            dist = round(((row - ore[0]) ** 2 + (col - ore[1]) ** 2) ** 0.5)
            recent_data.append([row, col, dist])
        print("It was the last probe.")
        return False

    assert check_solution(checkio, (1, 1)), "Example"
    assert check_solution(checkio, (9, 9)), "Bottom right"
    assert check_solution(checkio, (6, 6)), "Center"
