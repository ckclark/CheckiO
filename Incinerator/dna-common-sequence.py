from collections import defaultdict

def common(first, second):
    table = [[0] * (len(second) + 1) for _ in xrange(len(first) + 1)]
    for i1, c1 in enumerate(first, 1):
        for i2, c2 in enumerate(second, 1):
            if c1 == c2:
                table[i1][i2] = table[i1 - 1][i2 - 1] + 1
            else:
                table[i1][i2] = max(table[i1 - 1][i2], table[i1][i2 - 1])
    cache = defaultdict(set)
    cache[0, 0].add('')
    for i in xrange(len(first) + 1):
        for j in xrange(len(second) + 1):
            if i > 0 and j > 0 and table[i][j] == table[i - 1][j - 1] + 1 and first[i - 1] == second[j - 1]:
                cache[i, j].update(x + first[i - 1] for x in cache[i - 1, j - 1])
            if i > 0 and table[i][j] == table[i - 1][j]:
                cache[i, j].update(cache[i - 1, j])
            if j > 0 and table[i][j] == table[i][j - 1]:
                cache[i, j].update(cache[i, j - 1])
    return ','.join(sorted(set(cache[len(first), len(second)])))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert common("ACGTC", "TTACTC") == "ACTC", "One"
    assert common("CGCTA", "TACCG") == "CC,CG,TA", "Two"
    assert common("GCTT", "AAAAA") == "", "None"
