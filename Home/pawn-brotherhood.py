def safe_pawns(pawns):
    safe = 0

    chessboard = [[False] * 8 for _ in xrange(8)]
    for pawn in pawns:
        x, y = ord(pawn[0]) - ord('a'), ord(pawn[1]) - ord('1')
        chessboard[x][y] = True

    for pawn in pawns:
        x, y = ord(pawn[0]) - ord('a'), ord(pawn[1]) - ord('1')

        tx, ty = x + 1, y - 1
        if 0 <= tx < 8 and 0 <= ty < 8 and chessboard[tx][ty]:
            safe += 1
            continue

        tx, ty = x - 1, y - 1
        if 0 <= tx < 8 and 0 <= ty < 8 and chessboard[tx][ty]:
            safe += 1
            continue

    return safe

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
