def solution(stones, k):
    if k == 1:
        return min(stones)
    # k가 1이 아닌 경우
    answer = binary_search(k, stones, 1, max(stones))
    return answer


def is_cross(stones, answer, k):
    start = 0
    end = 0
    for i in range(1, len(stones)):
        if stones[i] <= answer:
            end = i
            if stones[i - 1] > answer:
                start = i
        if end - start == k - 1:
            return False
    return True


def binary_search(k, stones, start, end):
    if start == end:
        if is_cross(stones, start, k):
            return start + 1
        return start
    mid = (start + end) // 2
    if is_cross(stones, mid, k):
        return binary_search(k, stones, mid + 1, end)
    return binary_search(k, stones, start, mid)


print(solution([2, 4, 6, 3, 2, 1, 4, 2, 5, 1], 3))
