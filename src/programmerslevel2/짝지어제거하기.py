def solution(s):
    compressed = ["1"]
    for letter in s:
        if compressed[-1] == letter:
            compressed.pop()
        else:
            compressed.append(letter)
    if len(compressed) == 1:
        return 1
    else:
        return 0


print(solution("baabaa"))
