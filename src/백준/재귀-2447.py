# 인터넷 풀이 참고 (Pypy3으로 해야 통과)
import sys


def input():
    return sys.stdin.readline().rstrip()


N = int(input())

result = [[] for _ in range(N)]


def star(i, j, number):
    if (i // number) % 3 == 1 and (j // number) % 3 == 1:
        print(" ", end="")
    else:
        if number // 3 == 0:
            print("*", end="")
        else:
            star(i, j, number // 3)


for i in range(N):
    for j in range(N):
        star(i, j, N)
    print()
