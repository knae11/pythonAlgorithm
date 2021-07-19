import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())

graph = []
for i in range(n):
    line = list(map(int, input().split()))
    graph.append(line)

answer = [[1e9] * n for _ in range(n)]

answer[0] = graph[0]

for row in range(1, n):
    for col in range(n):
        for prev_col in range(n):
            if col == prev_col:
                continue
            answer[row][col] = min(answer[row - 1][prev_col] + graph[row][col], answer[row][col])

print(min(answer[-1]))
