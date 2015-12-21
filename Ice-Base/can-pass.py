def can_pass(matrix, first, second):
    matrix = map(list, matrix)
    w, h = len(matrix[0]), len(matrix)
    visited = set()
    stack = []
    visited.add(first)
    stack.append(first)
    while stack:
        cur = stack.pop()
        for d in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            nx, ny = cur[0] + d[0], cur[1] + d[1]
            if 0 <= nx < h and 0 <= ny < w and matrix[nx][ny] == matrix[cur[0]][cur[1]]:
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    stack.append((nx, ny))
    return second in visited

if __name__ == '__main__':
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 2), (0, 5)) == True, 'First example'
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 3), (6, 0)) == False, 'First example'
