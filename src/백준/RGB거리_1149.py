import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())

graph = []
for i in range(n):
    line = list(map(int, input().split()))
    graph.append(line)

answer = [[1e9] * 3 for _ in range(n)]

answer[0] = graph[0]

for row in range(1, n):
    for col in range(3):
        for prev_col in range(3):
            if col == prev_col:
                continue
            answer[row][col] = min(answer[row - 1][prev_col] + graph[row][col], answer[row][col])

print(min(answer[-1]))
