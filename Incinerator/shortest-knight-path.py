def checkio(cells):
    queue = [None] * 64
    head = tail = 0
    visited = set()
    start, end = cells.split('-')
    start = (ord(start[0]) - ord('a'), ord(start[1]) - ord('1'))
    end = (ord(end[0]) - ord('a'), ord(end[1]) - ord('1'))
    queue[head] = (start, 0)
    head += 1
    visited.add(start)
    while head != tail:
        cur, steps = queue[tail]
        if cur == end:
            return steps
        tail += 1
        for d in [(-1, 2), (1, 2), (1, -2), (-1, -2), (-2, 1), (2, 1), (2, -1), (-2, -1)]:
            nx, ny = cur[0] + d[0], cur[1] + d[1]
            if 0 <= nx < 8 and 0 <= ny < 8 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue[head] = ((nx, ny), steps + 1)
                head += 1
    return 0

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u"b1-d5") == 2, "1st example"
    assert checkio(u"a6-b8") == 1, "2nd example"
    assert checkio(u"h1-g2") == 4, "3rd example"
    assert checkio(u"h8-d7") == 3, "4th example"
    assert checkio(u"a1-h8") == 6, "5th example"
