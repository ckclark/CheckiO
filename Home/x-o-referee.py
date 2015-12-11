def checkio(game_result):

    row = [0] * 3
    col = [0] * 3
    diag = 0
    rdiag = 0
    for i in xrange(3):
        for j in xrange(3):
            if game_result[i][j] == 'O':
                row[i] += 1
                col[j] += 1
                if i == j:
                    diag += 1
                if i + j == 2:
                    rdiag += 1
            elif game_result[i][j] == 'X':
                row[i] -= 1
                col[j] -= 1
                if i == j:
                    diag -= 1
                if i + j == 2:
                    rdiag -= 1
    if -3 in row or -3 in col or diag == -3 or rdiag == -3:
        return 'X'
    if 3 in row or 3 in col or diag == 3 or rdiag == 3:
        return 'O'
    return 'D'

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        u"X.O",
        u"XX.",
        u"XOO"]) == "X", "Xs wins"
    assert checkio([
        u"OO.",
        u"XOX",
        u"XOX"]) == "O", "Os wins"
    assert checkio([
        u"OOX",
        u"XXO",
        u"OXX"]) == "D", "Draw"
    assert checkio([
        u"O.X",
        u"XX.",
        u"XOO"]) == "X", "Xs wins again"

