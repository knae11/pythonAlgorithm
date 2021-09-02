def solution(s):
    process = []
    for brace in s:
        if brace == "(":
            process.append(brace)
        else:
            if not process:
                return False
            if process[-1] == "(":
                process.pop()
            else:
                return False
    if len(process) > 0:
        return False
    return True


print(solution("(())()"))
