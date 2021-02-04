from collections import deque
from itertools import permutations


def checkVisited(weak, friends):
    index = 0
    visited = [False for _ in range(len(weak))]
    for friend in friends:
        dist = 0
        while friend >= dist and index < len(weak)-1:
            visited[index] = True
            index += 1
            dist += weak[index] - weak[index - 1]
        if friend >= dist:
            visited[index] = True
    if False in visited:
        return False
    else:
        return True


def solution(n, weak, dist):
    answer = 1
    if len(weak) == 1:
        return answer
    q = deque(weak)
    while answer <= len(dist):
        for friends in list(permutations(dist, answer)):
            for _ in range(len(weak)):
                point = q.popleft()
                q.append(point + n)
                if checkVisited(q, friends):
                    return answer
        answer += 1
    return -1


print(solution(50, [1, 25], [1, 1]))
