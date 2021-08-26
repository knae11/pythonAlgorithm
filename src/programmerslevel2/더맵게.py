import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) > 1:
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        if a >= K:
            return answer
        new_sco = a + (b * 2)
        answer += 1
        heapq.heappush(scoville, new_sco)
    for item in scoville:
        if item >= K:
            return answer

    return -1


print(solution([1, 2, 3, 9, 10, 12], 7))
