def solution(s):
    answer = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            sample = s[i:j]
            if sample == sample[::-1]:
                answer = max(answer, len(sample))
    return answer


print(solution("abacde"))
