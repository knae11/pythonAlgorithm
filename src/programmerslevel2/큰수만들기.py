
def solution(number, k):
    answer = ""
    # 초기값 셋팅
    stack = [number[0]]
    for n in number[1:]:
        while len(stack) > 0 and stack[-1] < n and k > 0:
            stack.pop()
            k -= 1
        stack.append(n)
    if k != 0:
        stack = stack[:-k]

    return ''.join(stack)


print(solution("4177252841", 4))
