from collections import deque


# 다시 푼 문: queue의 고정크기 또는 0을 넣어서 채워주는 것이 포인트!!
# 5번 시간초과: 매번 sum 계산 로직을 없애주니 통과!
def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_index = 0
    bridge = deque([0 for _ in range(bridge_length)], maxlen=bridge_length)
    total = 0
    while bridge:
        if truck_index < len(truck_weights):
            next_truck = truck_weights[truck_index]
            crossed_truck = bridge.popleft()
            total -= crossed_truck
            if total + next_truck > weight:
                bridge.append(0)
            else:
                total += next_truck
                bridge.append(next_truck)
                truck_index += 1
            answer += 1
        else:
            answer += len(bridge)
            break
    return answer


print(solution(2, 10, [7, 4, 5, 6]))
