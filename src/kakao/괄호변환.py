from collections import Counter


def balanced(given):
    counter = Counter(given)
    if counter['('] == counter[')']:
        return True
    return False


def correct(given):
    count = 0
    for i in given:
        if count < 0:
            return False
        if i == '(':
            count += 1
        else:
            count -= 1
    return True


def convert(given):
    result = ""
    for i in given:
        if i == ')':
            result += '('
        else:
            result += ')'
    return result


def solution(p):
    answer = ''
    if not p:
        return ''
    for i in range(1, len(p) + 1):
        if balanced(p[:i]):
            u = p[:i]
            v = p[i:]
            if correct(u):
                return u + solution(v)
            else:
                string = ""
                string += '('
                string += solution(v)
                string += ')'
                return string + convert(u[1:-1])

    return answer


print(solution("(()())()"))
