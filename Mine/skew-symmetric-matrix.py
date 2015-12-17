def checkio(matrix):
    return all(matrix[i][j] == -matrix[j][i] for i in xrange(len(matrix)) for j in xrange(len(matrix[0])))


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        [0, 1, 2],
        [-1, 0, 1],
        [-2, -1, 0]]) == True, "1st example"
    assert checkio([
        [0, 1, 2],
        [-1, 1, 1],
        [-2, -1, 0]]) == False, "2nd example"
    assert checkio([
        [0, 1, 2],
        [-1, 0, 1],
        [-3, -1, 0]]) == False, "3rd example"
