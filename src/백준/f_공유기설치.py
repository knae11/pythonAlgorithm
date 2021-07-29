import sys

sys.setrecursionlimit(10**6)
def input():
    return sys.stdin.readline().rstrip()


N, M = map(int, input().split())
min_home = 1e9
max_home = 0
homes = set()
for _ in range(N):
    num = int(input())
    homes.add(num)
    min_home = min(min_home, num)
    max_home = max(max_home, num)
answer = 1e9


def find_closest(mid):
    left_mid = mid
    right_mid = mid
    while True:
        if left_mid in homes:
            return left_mid
        if right_mid in homes:
            return right_mid
        left_mid -= 1
        right_mid += 1


def install_wifi(start, end, count):
    global answer
    if count < 1:
        return
    mid = (start + end) // 2
    if start >= mid or end < mid:
        return
    if mid in homes:
        answer = min(answer, end - mid, mid - start)
        install_wifi(start, mid, count - 1)
        install_wifi(mid + 1, end, count - 1)
    else:
        mid = find_closest(mid)
        answer = min(answer, end - mid, mid - start)
        install_wifi(start, mid, count - 1)
        install_wifi(mid + 1, end, count - 1)


install_wifi(min_home, max_home, M - 2)

print(answer)
