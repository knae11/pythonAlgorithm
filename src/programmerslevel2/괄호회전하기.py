def check(s):
    pairs = ["()", "[]", "{}"]
    while True:
        count = 0
        for pair in pairs:
            if pair in s:
                count += 1
        if count == 0:
            break
        s = s.replace("()", "")
        s = s.replace("{}", "")
        s = s.replace("[]", "")
    if len(s) != 0:
        return False
    return True


def solution(s):
    answer = 0
    for i in range(len(s)):
        n_s = s[i:] + s[:i]
        if check(n_s):
            answer += 1
    return answer


print(solution("[](){}"))
