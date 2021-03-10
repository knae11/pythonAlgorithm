from collections import deque


def solution(priorities, location):
    answer = 0

    queue = deque()
    answer_list = []
    # enumerate를 사용하면 간편하게 셋팅가능
    for i in range(len(priorities)):
        queue.append((priorities[i], i))

    while queue:
        candidate = queue.popleft()
        # 이 문제의 경우 마지막까지 해당 번호가 나오지 않아서 queue가 비는경우를 확인해 주어야함!
        if not queue:
            return len(answer_list) + 1
        # any로 체크 가능
        array = [item[0] for item in queue]
        if candidate[0] < max(array):
            queue.append(candidate)
        else:
            answer_list.append(candidate)
            if candidate[1] == location:
                return len(answer_list)
    return answer
