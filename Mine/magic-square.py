def dfs(data, target, N, x, y, row, col, diag, rdiag, unused):
    global ans
    if x == N:
        if all(z == target for z in row + col) and diag == target and rdiag == target:
            ans = [row[:] for row in data]
            return True
    elif y == N:
        if dfs(data, target, N, x + 1, 0, row, col, diag, rdiag, unused):
            return True
    else:
        if data[x][y]:
            if dfs(data, target, N, x, y + 1, row, col, diag, rdiag, unused):
                return True
        else:
            for u in unused:
                unused.remove(u)
                data[x][y] = u
                row[x] += u
                col[y] += u
                if x == y:
                    diag += u
                if x + y == N - 1:
                    rdiag += u
                if row[x] <= target and col[y] <= target and diag <= target and rdiag <= target:
                    if dfs(data, target, N, x, y + 1, row, col, diag, rdiag, unused):
                        return True
                data[x][y] = 0
                row[x] -= u
                col[y] -= u
                if x == y:
                    diag -= u
                if x + y == N - 1:
                    rdiag -= u
                unused.add(u)

def checkio(data):
    global ans
    N = len(data)
    row = [0] * N
    col = [0] * N
    diag = 0
    rdiag = 0
    unused = set(xrange(1, N * N + 1))
    target = sum(unused) / N
    for i in xrange(N):
        for j in xrange(N):
            v = data[i][j]
            unused.discard(v)
            row[i] += v
            col[j] += v
            if i == j:
                diag += v
            if i + j == N - 1:
                rdiag += v
    assert dfs(data, target, N, 0, 0, row, col, diag, rdiag, unused)
    return ans

if __name__ == '__main__':
    #This part is using only for self-testing.
    def check_solution(func, in_square):
        SIZE_ERROR = "Wrong size of the answer."
        MS_ERROR = "It's not a magic square."
        NORMAL_MS_ERROR = "It's not a normal magic square."
        NOT_BASED_ERROR = "Hm, this square is not based on given template."
        result = func(in_square)
        #check sizes
        N = len(result)
        if len(result) == N:
            for row in result:
                if len(row) != N:
                    print(SIZE_ERROR)
                    return False
        else:
            print(SIZE_ERROR)
            return False
        #check is it a magic square
        # line_sum = (N * (N ** 2 + 1)) / 2
        line_sum = sum(result[0])
        for row in result:
            if sum(row) != line_sum:
                print(MS_ERROR)
                return False
        for col in zip(*result):
            if sum(col) != line_sum:
                print(MS_ERROR)
                return False
        if sum([result[i][i] for i in range(N)]) != line_sum:
            print(MS_ERROR)
            return False
        if sum([result[i][N - i - 1] for i in range(N)]) != line_sum:
            print(MS_ERROR)
            return False

        #check is it normal ms
        good_set = set(range(1, N ** 2 + 1))
        user_set = set([result[i][j] for i in range(N) for j in range(N)])
        if good_set != user_set:
            print(NORMAL_MS_ERROR)
            return False
        #check it is the square based on input
        for i in range(N):
            for j in range(N):
                if in_square[i][j] and in_square[i][j] != result[i][j]:
                    print(NOT_BASED_ERROR)
                    return False
        return True


    assert check_solution(checkio,
                          [[2, 7, 6],
                           [9, 5, 1],
                           [4, 3, 0]]), "1st example"

    assert check_solution(checkio,
                          [[0, 0, 0],
                           [0, 5, 0],
                           [0, 0, 0]]), "2nd example"

    assert check_solution(checkio,
                          [[1, 15, 14, 4],
                           [12, 0, 0, 9],
                           [8, 0, 0, 5],
                           [13, 3, 2, 16]]), "3rd example"
