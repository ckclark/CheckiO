def on_edge(point, edge):
    p0, p1 = edge
    if (p0[0] - point[0]) * (p1[1] - point[1]) == (p1[0] - point[0]) * (p0[1] - point[1]):
        # same slope
        if p0[0] <= point[0] <= p1[0] or p1[0] <= point[0] <= p0[0]:
            if p0[1] <= point[1] <= p1[1] or p1[1] <= point[0] <= p0[1]:
                return True
    return False

def ray_casting(edges, point):
    # https://en.wikipedia.org/wiki/Point_in_polygon#Ray_casting_algorithm
    cross_x = []
    for edge in edges:
        # ignore horizontal line where y = the y value of point since on_edge() will cover this case
        if edge[0][1] > edge[1][1] and edge[1][1] == point[1]:
            cross_x.append((edge[1][0], 1))
        elif edge[0][1] < edge[1][1] and edge[0][1] == point[1]:
            cross_x.append((edge[0][0], 1))
        elif (edge[0][1] - point[1]) * (edge[1][1] - point[1]) < 0:
            # calculate the cross x value as (num, den) format, and ensure den > 0
            x = (edge[0][0] * (edge[0][1] - edge[1][1]) - (edge[0][0] - edge[1][0]) * (edge[0][1] - point[1]), edge[0][1] - edge[1][1])
            if x[1] < 0:
                x = (-x[0], -x[1])
            cross_x.append(x)
    cross_x.append((point[0], 1))
    cross_x.sort(cmp=lambda a, b: cmp(a[0] * b[1], b[0] * a[1]))
    return cross_x.index((point[0], 1)) % 2 == 1

def is_inside(polygon, point):
    edges = []
    n = len(polygon)
    for i in xrange(n - 1, -1, -1):
        edges.append([polygon[i], polygon[i - 1]])
    for edge in edges:
        if on_edge(point, edge):
            return True
    return ray_casting(edges, point)

if __name__ == '__main__':
    assert is_inside(((1, 1), (1, 3), (3, 3), (3, 1)),
                     (2, 2)) == True, "First"
    assert is_inside(((1, 1), (1, 3), (3, 3), (3, 1)),
                     (4, 2)) == False, "Second"
    assert is_inside(((1, 1), (4, 1), (2, 3)),
                     (3, 2)) == True, "Third"
    assert is_inside(((1, 1), (4, 1), (1, 3)),
                     (3, 3)) == False, "Fourth"
    assert is_inside(((2, 1), (4, 1), (5, 3), (3, 4), (1, 3)),
                     (4, 3)) == True, "Fifth"
    assert is_inside(((2, 1), (4, 1), (3, 2), (3, 4), (1, 3)),
                     (4, 3)) == False, "Sixth"
    assert is_inside(((1, 1), (3, 2), (5, 1), (4, 3), (5, 5), (3, 4), (1, 5), (2, 3)),
                     (3, 3)) == True, "Seventh"
    assert is_inside(((1, 1), (1, 5), (5, 5), (5, 4), (2, 4), (2, 2), (5, 2), (5, 1)),
                     (4, 3)) == False, "Eighth"
