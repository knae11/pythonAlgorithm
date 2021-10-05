# visited 조건 잘 처리하기!!
from collections import deque


def bfs(i, n, computers, visited):
    queue = deque()
    queue.append(i)
    while queue:
        k = queue.popleft()
        for j in range(n):
            if not visited[j] and computers[k][j] == 1:
                visited[j] = True
                queue.append(j)


def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            bfs(i, n, computers, visited)
            answer += 1
    return answer
