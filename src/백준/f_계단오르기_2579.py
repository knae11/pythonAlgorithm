import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())

stairs = []
accu = []
for _ in range(n):
    num = int(input())
    stairs.append(num)
    accu.append(num)

answer = 0

if n < 3:
    answer = sum(stairs)

# print(accu)


def go_up(index, conti, result):
    global answer
    if conti >= 2:
        return
    if index > n - 1:
        return
    if index == n - 1:
        answer = max(answer, result + stairs[index])
        return

    go_up(index + 1, conti + 1, result + stairs[index])
    go_up(index + 2, 0, result + stairs[index])


go_up(0, 0, 0)
go_up(1, 0, 0)

print(answer)
