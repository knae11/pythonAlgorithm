# 동적계획법 : 큰문제를 작은 문제로 나누어서 해결
# 탑다운(메모이제이션 활용),  <<<권장<<< 보텀업(DP 테이블 활용)

# 1로 만들기 예제 - 보텀업

# 앞의 계산된 결과를 저장하기 위한 DP 테이블
x = 100
d = [0] * 30001  # 유한함

for i in range(2, x + 1):
    # 현재 수에서 1을 빼는 경우 횟수 1 추가 (모든 경우 가능)
    d[i] = d[i - 1] + 1
    # 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

# 피보나치 탑타운
t = [0] * 100


def pibo_top_down(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = pibo_top_down(x - 1) + pibo_top_down(x - 2)
    return d[x]


# 피보나치 보텀업 (권장)
b = [0] * 100

d[1] = 1
d[2] = 1

n = 99
for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]
