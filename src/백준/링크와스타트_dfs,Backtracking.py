
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

'''
# 다른사람 풀이 참고
import sys
from itertools import combinations


def input():
    return sys.stdin.readline().rstrip()


N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
row = [sum(i) for i in arr]
col = [sum(i) for i in zip(*arr)]
print(arr, row, col)  # row-> 0,1,2,3 열의 합, col -> 0,1,2,3 행의 합
new_arr = [i + j for i, j in zip(row, col)]  # 각 0,0 // 1,1 // 2,2 // 3,3 -> 열,행의 조합의 합
total_sum = sum(new_arr) // 2
print(new_arr, total_sum)
result = float('inf')
for num in range(1, N // 2 + 1):
    for combi in combinations(new_arr, num):
        result = min(result, abs(total_sum - sum(combi)))
        if result == 0:
            break
    if result == 0:
        break

print(result)
'''