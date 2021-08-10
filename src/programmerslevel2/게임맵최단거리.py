from collections import deque


def solution(maps):
    I = len(maps)
    J = len(maps[0])
    queue = deque()
    queue.append((0, 0))
    moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    while queue:
        i, j = queue.popleft()
        for k in range(4):
            ni = i + moves[k][0]
            nj = j + moves[k][1]
            if not (0 <= ni < I and 0 <= nj < J):
                continue
            if maps[ni][nj] == 1:
                maps[ni][nj] = maps[i][j] + 1
                queue.append((ni, nj))
    if maps[I - 1][J - 1] == 1:
        return -1
    return maps[I - 1][J - 1]


solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1],
          [0, 0, 0, 0, 1]])
