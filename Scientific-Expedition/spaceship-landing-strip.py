def checkio(landing_map):
    w, h = len(landing_map[0]), len(landing_map)
    subsum = [[0] * w for _ in xrange(h)]
    subsum[0] = map('GS'.__contains__, landing_map[0])

    for i in xrange(1, h):
        for j in xrange(w):
            if landing_map[i][j] in 'GS':
                subsum[i][j] = subsum[i - 1][j] + 1
    m = 0
    for i in xrange(h):
        stack = [(-1, -1)]
        for j in xrange(w):
            while stack and stack[-1][1] >= subsum[i][j]:
                pj, ps = stack.pop()
                m = max(m, ((j - 1) - stack[-1][0]) * ps)
            stack.append((j, subsum[i][j]))

        while stack and stack[-1][1] >= 0:
            pj, ps = stack.pop()
            m = max(m, ((w - 1) - stack[-1][0]) * ps)
    return m

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([u'GGTGG',
                    u'TGGGG',
                    u'GSSGT',
                    u'GGGGT',
                    u'GWGGG',
                    u'RGTRT',
                    u'RTGWT',
                    u'WTWGR']) == 9, 'Classic'
    assert checkio([u'G']) == 1, 'One cell - one variant'
    assert checkio([u'GS',
                    u'GS']) == 4, 'Four good cells'
    assert checkio([u'GT',
                    u'GG']) == 2, 'Four cells, but with a tree'
