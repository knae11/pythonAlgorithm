import sys

n = int(sys.stdin.readline().rstrip())
graph = []
for i in range(n):
    line = list(map(int, sys.stdin.readline().rstrip().split()))
    graph.append(line)

answer = 1e9


def calculate(team):
    count = 0
    for i in team:
        for j in team:
            count += graph[i][j]
    return count


def check(visited, r, depth, start_n):
    global answer
    # 종료조건
    if start_n >= n:
        return
    a_list = []
    b_list = []
    for i in range(n):
        if visited[i]:
            a_list.append(i)
        else:
            b_list.append(i)
    a = calculate(a_list)
    b = calculate(b_list)
    answer = min(answer, abs(a - b))

    for q in range(start_n, n):
        visited[q] = True
        check(visited, r, depth + 1, q + 1)
        visited[q] = False
    return


visited = [False for _ in range(n)]
check(visited, n // 2, 0, 0)

print(answer)
