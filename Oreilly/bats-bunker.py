from collections import defaultdict
import heapq

def _siftdown(heap, startpos, pos):
    newitem = heap[pos]
    # Follow the path to the root, moving parents down until finding a place
    # newitem fits.
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if newitem < parent:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem
heapq._siftdown = _siftdown

class MAX(object):
    def __gt__(self, other):
        # always greater than others
        return True

class Bat(object):
    def __init__(self, idx):
        self.dis = MAX()
        self.idx = idx

    def __lt__(self, other):
        return self.dis < other.dis

def cross(w, h, p, a, b, c):
    if p[0] < 0 or p[0] >= h or p[1] < 0 or p[1] >= w:
        return False

    t = a * p[0] + b * p[1] + c
    for d in ((0, 1), (1, 1), (1, 0)):
        nx, ny = p[0] + d[0], p[1] + d[1]
        s = a * nx + b * ny + c
        if t * s <= 0:
            return True
    return False

def cal_dis(bunker, p1, p2):
    w, h = len(bunker[0]), len(bunker)
    if p2[0] > p1[0]:
        dx = 1
    elif p2[0] < p1[0]:
        dx = -1
    else:
        dx = 0

    if p2[1] > p1[1]:
        dy = 1
    elif p2[1] < p1[1]:
        dy = -1
    else:
        dy = 0

    a = 2 * (p2[1] - p1[1])
    b = -2 * (p2[0] - p1[0])
    c = (p2[0] - p1[0]) * (2 * p1[1] + 1) - (p2[1] - p1[1]) * (2 * p1[0] + 1)
    x, y = p1
    while (x, y) != p2:
        tx, ty = x + dx, y + dy
        if (tx, ty) != (x, y) and cross(w, h, (tx, ty), a, b, c):
            if bunker[tx][ty] == 'W' and dx * (p2[0] - tx) >= 0 and dy * (p2[1] - ty) >= 0:
                return None
            nx, ny = tx, ty
        tx, ty = x + dx, y
        if (tx, ty) != (x, y) and cross(w, h, (tx, ty), a, b, c):
            if bunker[tx][ty] == 'W' and dx * (p2[0] - tx) >= 0 and dy * (p2[1] - ty) >= 0:
                return None
            nx, ny = tx, ty
        tx, ty = x, y + dy
        if (tx, ty) != (x, y) and cross(w, h, (tx, ty), a, b, c):
            if bunker[tx][ty] == 'W' and dx * (p2[0] - tx) >= 0 and dy * (p2[1] - ty) >= 0:
                return None
            nx, ny = tx, ty
        x, y = nx, ny
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** .5

def checkio(bunker):
    w, h = len(bunker[0]), len(bunker)
    bats = []
    dis = dict()
    adj = defaultdict(list)
    for i in xrange(h):
        for j in xrange(w):
            if bunker[i][j] == 'B':
                bats.append((i, j))
            elif bunker[i][j] == 'A':
                alpha_i = len(bats)
                bats.append((i, j))

    for i in xrange(len(bats)):
        for j in xrange(i):
            d = cal_dis(bunker, bats[i], bats[j])
            if d is not None:
                dis[i, j] = dis[j, i] = d
                adj[i].append(j)
                adj[j].append(i)


    bat_list = map(Bat, xrange(len(bats)))
    dijkstra = bat_list[:]
    bat_list[alpha_i].dis = 0
    heapq.heapify(dijkstra)
    while True:
        cur = heapq.heappop(dijkstra)

        if bats[cur.idx] == (0, 0):
            return cur.dis

        for adj_bat in adj[cur.idx]:
            if cur.dis + dis[cur.idx, adj_bat] < bat_list[adj_bat].dis:
                bat_list[adj_bat].dis = cur.dis + dis[cur.idx, adj_bat]
                heapq._siftdown(dijkstra, 0, dijkstra.index(bat_list[adj_bat]))
    return float("inf")


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    def almost_equal(checked, correct, significant_digits=2):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(checkio([
        "B--",
        "---",
        "--A"]), 2.83), "1st example"
    assert almost_equal(checkio([
        "B-B",
        "BW-",
        "-BA"]), 4), "2nd example"
    assert almost_equal(checkio([
        "BWB--B",
        "-W-WW-",
        "B-BWAB"]), 12), "3rd example"
    assert almost_equal(checkio([
        "B---B-",
        "-WWW-B",
        "-WA--B",
        "-W-B--",
        "-WWW-B",
        "B-BWB-"]), 9.24), "4th example"
