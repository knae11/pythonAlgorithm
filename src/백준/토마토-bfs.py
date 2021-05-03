import sys
from collections import deque

# https://www.acmicpc.net/problem/7576

m, n = map(int, sys.stdin.readline().rstrip().split())
board = []
for _ in range(n):
    line = list(map(int, sys.stdin.readline().rstrip().split()))
    board.append(line)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque()

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            queue.append((i, j))

def bfs():
    while (queue):
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or board[nx][ny] != 0:
                continue
            board[nx][ny] = board[x][y] + 1
            queue.append((nx, ny))

    answer = -1
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                return -1
            else:
                answer = max(answer, board[i][j])
    return answer-1
print(bfs())



