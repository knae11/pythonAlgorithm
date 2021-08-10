import sys
import heapq


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
consulting = []
for _ in range(N):
    day, cost = map(int, input().split())
    consulting.append((day, cost))

results = []


def dfs(index, result):
    day, cost = consulting[index][0], consulting[index][1]
    next_index = index + day
    if next_index == N:
        heapq.heappush(results, -(result+cost))
        return
    elif next_index > N:
        heapq.heappush(results, -result)
        return
    else:
        for i in range(next_index, N):
            dfs(i, result + cost)


for i in range(N):
    dfs(i, 0)

print(-results[0])


'''
다른풀이 구경: dp 활용
import sys

input = sys.stdin.readline

n = int(input())
pays = [list(map(int, input().split())) for _ in range(n)]

table = [0] * (n + 2)
for i in range(1, n + 1):
    time, pay = pays[i - 1]
    max_pay = max(table[: i + 1])
    if i + time > n + 1:
        continue
    table[i + time] = max(max_pay + pay, table[i + time])

print(max(table))
'''