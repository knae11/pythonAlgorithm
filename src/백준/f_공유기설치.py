import sys


def input():
    return sys.stdin.readline().rstrip()


N, M = map(int, input().split())

homes = []
for _ in range(N):
    homes.append(int(input()))


homes.sort()

lines = [0] * (homes[-1] + 1)
for home in homes:
    lines[home] = 1

answer = 1e9


def find_closest(mid):
    left_mid = mid
    right_mid = mid
    while True:
        if lines[left_mid] == 1:
            return left_mid
        if lines[right_mid] == 1:
            return right_mid
        left_mid -= 1
        right_mid += 1


def install_wifi(start, end, count):
    global answer
    if count < 1:
        return
    mid = (start + end) // 2
    if start >= mid or end <= mid:
        return
    if lines[mid] == 1:
        answer = min(answer, end - mid, mid - start)
        install_wifi(start, mid, count - 1)
        install_wifi(mid + 1, end, count - 1)
    else:
        mid = find_closest(mid)
        answer = min(answer, end - mid, mid - start)
        install_wifi(start, mid, count - 1)
        install_wifi(mid + 1, end, count - 1)


install_wifi(homes[0], homes[-1], M - 2)

print(answer)
