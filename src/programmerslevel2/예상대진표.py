def solution(n, a, b):
    answer = 0
    if a > b:
        a, b = b, a
    while True:
        if a == b:
            return answer
        a = a // 2 + a % 2
        b = b // 2 + b % 2
        answer = answer + 1


print(solution(8, 7, 4))
