from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_queue = deque(truck_weights)
    bridge = deque()
    # todo: bridge에 트럭이 올라온다 -> length 만큼 카운트
    # 무게가 넘지 않고 공간이 비면 다음 차가 올라옴 +1

    while truck_queue:
        # bridge에 트럭을 올림
        bridge.append(truck_queue.popleft())
        answer += 1
        # 무게가 괜찮다면 트럭을 더 올림
        if sum(bridge) > weight:
            truck_queue.appendleft(bridge[-1])
            bridge.remove(bridge[-1])
            break
        print(answer, len(bridge))

        bridge.clear()

    return answer


print(solution(2, 10, [7, 4, 5, 6]))
