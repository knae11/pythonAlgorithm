import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
M = int(input())
computers = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    # 양방향으로 넣어주어야 함
    computers[a].append(b)
    computers[b].append(a)

answer = 0

queue = deque()
queue.append(1)
visited[1] = True
while queue:
    number = queue.popleft()
    for num in computers[number]:
        if not visited[num]:
            answer += 1
            visited[num] = True
            queue.append(num)
print(answer)
