import sys

m, n = map(int, sys.stdin.readline().rstrip().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))


def solution(m, n, graph):
    new_board = [[0 for _ in range(m)] for _ in range(n)]
    new_board[0][0] = graph[0][0]
    if n == 1:
        count = 0
        for i in range(m):
            count += graph[0][i]
        return count
    if m == 1:
        count = 0
        for i in range(n):
            count += graph[i][0]
        return count
    new_board[0][1] = graph[0][0] + graph[0][1]
    new_board[1][0] = graph[0][0] + graph[1][0]
    for i in range(1, n):
        for j in range(1, m):
            new_board[i][j] = max(new_board[i - 1][j] + graph[i][j], new_board[i][j - 1] + graph[i][j])
    return new_board[n-1][m-1]

print(solution(m, n, graph))
