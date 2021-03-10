from collections import deque


def solution(priorities, location):
    answer = 0

    queue = deque()
    answer_list = []

    for i in range(len(priorities)):
        queue.append((priorities[i], i))

    while queue:
        candidate = queue.popleft()
        if not queue:
            return len(answer_list) + 1
        array = [item[0] for item in queue]
        if candidate[0] < max(array):
            queue.append(candidate)
        else:
            answer_list.append(candidate)
            if candidate[1] == location:
                return len(answer_list)
    return answer
