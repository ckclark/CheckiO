def cross_product(a, b, c, d):
    return a * d - b * c

def checkio(data):
    left = data[0][0]
    bottom = data[0][1]
    start = 0
    for i, p in enumerate(data):
        if p[0] < left:
            left = p[0]
            bottom = p[1]
            start = i
        elif p[0] == left and p[1] < bottom:
            bottom = p[1]
            start = i

    ans = [start]
    cur = data[start]
    while True:
        nxt = None
        for i, d in enumerate(data):
            if d != cur:
                if nxt is None:
                    nxt = d
                    nxti = i
                else:
                    cp = cross_product(nxt[0] - cur[0], nxt[1] - cur[1], d[0] - cur[0], d[1] - cur[1])
                    if cp > 0:
                        nxt = d
                        nxti = i
                    elif cp == 0 and abs(d[0] - cur[0]) + abs(d[1] - cur[1]) < abs(nxt[0] - cur[0]) + abs(nxt[1] - cur[1]):
                        nxt = d
                        nxti = i
        if nxti == start:
            break
        ans.append(nxti)
        cur = nxt
    return ans

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(
        [[7, 6], [8, 4], [7, 2], [3, 2], [1, 6], [1, 8], [4, 9]]
    ) == [4, 5, 6, 0, 1, 2, 3], "First example"
    assert checkio(
        [[3, 8], [1, 6], [6, 2], [7, 6], [5, 5], [8, 4], [6, 8]]
    ) == [1, 0, 6, 3, 5, 2], "Second example"
