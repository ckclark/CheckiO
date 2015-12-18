def recall_password(cipher_grille, ciphered_password):
    grille = sorted((x, y) for x in xrange(4) for y in xrange(4) if cipher_grille[x][y] == 'X')
    ans = []
    for i in xrange(4):
        ans.extend(ciphered_password[g[0]][g[1]] for g in grille)
        grille = sorted((y, 3 - x) for (x, y) in grille)
    return ''.join(ans)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
