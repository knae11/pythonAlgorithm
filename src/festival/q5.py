import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
graph = []
for _ in range(m):
    graph.append([i for i in sys.stdin.readline().rstrip()])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[False for _ in range(n)] for _ in range(m)]


def find_way(i, j, count):
    if i == m - 1:
        if graph[i][j] == '.':
            print(count)
            return count

    for k in range(4):
        ni = i + dx[k]
        nj = j + dy[k]
        if ni >= m or ni < 0 or nj >= n or nj < 0:
            continue
        if visited[i][j]:
            continue
        visited[i][j] = True
        if graph[ni][nj] == '.':
            if ni == i:
                find_way(ni, nj, count + 1)
            else:
                find_way(ni, nj, count)
        return 1e9

def solution():
    answer = 1e9
    for j in range(n):
        if graph[0][j] == 'c':
            answer = min(answer, find_way(0, j, 0))
    if answer == 1e9:
        return -1
    return answer


print(solution())
