import math
from collections import deque


def solution(progresses, speeds):
    answer = []
    items = deque()
    for i in range(len(speeds)):
        remains = 100 - progresses[i]
        left = math.ceil(remains / speeds[i])
        items.append(left)

    previous = 0
    count = 0
    while items:
        item = items.popleft()
        if previous == 0:
            count += 1
            previous = item
            continue
        if item > previous:
            previous = item
            answer.append(count)
            count = 0
            count += 1
        else:
            count += 1
    answer.append(count)
    return answer


print(solution([93, 30, 55], [1, 30, 5]))
