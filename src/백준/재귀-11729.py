import sys


def input():
    return sys.stdin.readline().rstrip()


N = int(input())

result = []


def hanoi(start, middle, target, n):
    if n == 1:
        result.append([start, target])
        return
    hanoi(start, target, middle, n - 1)
    result.append([start, target])
    hanoi(middle, start, target, n - 1)


hanoi("1", "2", "3", N)
print(len(result))
for i in range(len(result)):
    print(" ".join(result[i]))
