import sys


def input():
    return sys.stdin.readline().rstrip()


N, M = map(int, input().split())
homes = []
for _ in range(N):
    homes.append(int(input()))
answer = 1e9

homes.sort()

answer = 0
# 최소간격
min_dist = 1
# 최대간격
max_dist = homes[-1] - homes[0]

while min_dist <= max_dist:
    # 중간 gap 설정
    mid_gap = (min_dist + max_dist) // 2
    curr_position = homes[0]
    count = 1
    # 전체 homes 를 돌면서 gap 이상인 경우마다 공유기 설치
    for i in range(1, N):
        if homes[i] >= curr_position + mid_gap:
            count += 1
            curr_position = homes[i]
    # gap 마다 설치했는데 공유기가 너무 많다면? gap 을 늘려줌
    if count >= M:
        # while 문 종료를 대비하여 answer 마킹
        answer = mid_gap
        min_dist = mid_gap + 1
    else:
        max_dist = mid_gap - 1
print(answer)

# 인터넷 풀이 참고
# 간격을 알아내야 한다면? 이분 탐색도 간격을 기준으로 해야한다!
