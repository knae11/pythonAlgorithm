def hanoi(n, start_poll, end_poll, between_poll, result):
    if n == 1:
        result.append([start_poll, end_poll])
        return
    hanoi(n - 1, start_poll, between_poll, end_poll, result)
    result.append([start_poll, end_poll])
    hanoi(n - 1, between_poll, end_poll, start_poll, result)


def solution(n):
    answer = []
    hanoi(n, 1, 3, 2, answer)
    return answer
'''
참고 풀이

def hanoi(f, t, m, n):
    if n == 0:
        return []

    return hanoi(f, m, t, n-1) + [[f, t]] + hanoi(m, t, f, n-1)


def solution(n):
    return hanoi(1, 3, 2, n)
'''

print(solution(2))
