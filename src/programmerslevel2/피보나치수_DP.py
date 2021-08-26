# 전형적인 DP
# 인터넷 풀이 참고

import sys
sys.setrecursionlimit(10**6)

d = [0 for _ in range(100001)]


def dp(k):
    if k == 1:
        return 1
    if k == 0:
        return 0

    if d[k] != 0:
        return d[k] % 1234567
    d[k] = dp(k - 1) + dp(k - 2)
    return d[k] % 1234567


def solution(n):
    d[1] = 1
    answer = dp(n)
    return answer


print(solution(5))
