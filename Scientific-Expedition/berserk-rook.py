def toPos(notation):
    return (ord(notation[0]) - ord('a'), ord(notation[1]) - ord('1'))

def dfs(table, cur, cap):
    global max_cap
    if cap > max_cap:
        max_cap = cap
    for i in xrange(cur[1] - 1, -1, -1):
        if table[cur[0]][i]:
            table[cur[0]][i] = False
            dfs(table, (cur[0], i), cap + 1)
            table[cur[0]][i] = True
            break

    for i in xrange(cur[1] + 1, 8):
        if table[cur[0]][i]:
            table[cur[0]][i] = False
            dfs(table, (cur[0], i), cap + 1)
            table[cur[0]][i] = True
            break

    for i in xrange(cur[0] - 1, -1, -1):
        if table[i][cur[1]]:
            table[i][cur[1]] = False
            dfs(table, (i, cur[1]), cap + 1)
            table[i][cur[1]] = True
            break

    for i in xrange(cur[0] + 1, 8):
        if table[i][cur[1]]:
            table[i][cur[1]] = False
            dfs(table, (i, cur[1]), cap + 1)
            table[i][cur[1]] = True
            break

def berserk_rook(berserker, enemies):
    table = [[False] * 8 for _ in xrange(8)]
    berserker = toPos(berserker)
    for enemy in enemies:
        enemy = toPos(enemy)
        table[enemy[0]][enemy[1]] = True
    global max_cap
    max_cap = 0
    dfs(table, berserker, 0)
    return max_cap

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert berserk_rook(u'd3', {u'd6', u'b6', u'c8', u'g4', u'b8', u'g6'}) == 5, "one path"
    assert berserk_rook(u'a2', {u'f6', u'f2', u'a6', u'f8', u'h8', u'h6'}) == 6, "several paths"
    assert berserk_rook(u'a2', {u'f6', u'f8', u'f2', u'a6', u'h6'}) == 4, "Don't jump through"
