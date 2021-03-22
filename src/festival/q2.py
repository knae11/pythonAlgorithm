# fail

import sys
length = sys.stdin.readline()
road = sys.stdin.readline()

answer = 0


def dfs(road, index):
    global answer
    if index >= len(road):
        return
    if road[index] == "0":
        return
    if index == (len(road) - 1):
        answer += 1
        return
    dfs(road, index + 1)
    dfs(road, index + 2)


road_info = [i for i in road]
dfs(road_info, 0)

print(answer)
