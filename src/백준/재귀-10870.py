import sys


def input():
    return sys.stdin.readline().rstrip()


N = int(input())


def recur(number, a, b):
    if number == N:
        return a + b
    return recur(number + 1, b, a + b)


if N == 0:
    print(0)
elif N == 1:
    print(1)
else:
    print(recur(2, 0, 1))
