from math import gcd


def lcm(a, b):
    return a * b // gcd(a, b)


def solution(arr):
    answer = 1
    for item in arr:
        answer = lcm(answer, item)
    return answer


print(solution([2, 6, 8, 14]))
