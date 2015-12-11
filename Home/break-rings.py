def break_rings(rings):
    nodes = sorted(reduce(set.union, rings))
    size = len(nodes)
    curmin = size - 1

    for i in xrange(1 << size):
        bit_one = 0
        j = 0
        t = i
        selected = set()
        while t > 0:
            j += 1
            if t & 1:
                bit_one += 1
                selected.add(j)
            t >>= 1
        if bit_one > curmin:
            continue
        for ring in rings:
            if all(r not in selected for r in ring):
                break
        else:
            curmin = bit_one
    return curmin

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert break_rings(({1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {4, 6})) == 3, "example"
    assert break_rings(({1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4})) == 3, "All to all"
    assert break_rings(({5, 6}, {4, 5}, {3, 4}, {3, 2}, {2, 1}, {1, 6})) == 3, "Chain"
    assert break_rings(({8, 9}, {1, 9}, {1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {8, 7})) == 5, "Long chain"
