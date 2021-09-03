def solution(n):
    answer = 0
    for i in range(1, n):
        result = 0
        while result < n:
            result += i
            if result == n:
                answer += 1
                break
            i += 1

    return answer + 1


print(solution(15))
