# 유클리드 호제법으로 계산하는 최대공약수 구하기
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def solution(w, h):
    # 사이에 지나가는 사각형의 갯수는 ( 가로 + 세로 - 가로세로의_최대공약수 )
    return w * h - (w + h - gcd(w, h))


print(solution(8, 12))
