# 백준문제 계단오르기

import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())

stairs = []
for _ in range(n):
    stairs.append(int(input()))


def solution():
    dp = [0] * n
    if n < 3:
        return sum(stairs)

    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    dp[2] = max(stairs[2] + stairs[1], stairs[2] + dp[0])

    for i in range(3, n):
        dp[i] = max(dp[i - 2] + stairs[i], stairs[i] + stairs[i - 1] + dp[i - 3])
    return dp[-1]


print(solution())
