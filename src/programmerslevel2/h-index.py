# 문제 잘읽자!
def solution(citations):
    answer = 0
    citations.sort()
    for i in range(len(citations), 0, -1):
        k = i
        more = 0
        same = 0
        for cita in citations[::-1]:
            if cita > k:
                more += 1
            elif cita == k:
                same += 1
            else:
                break

        if more + same >= k >= len(citations) - (more + same) + same:
            return k

    return answer


print(solution([3, 0, 6, 1, 5]))
