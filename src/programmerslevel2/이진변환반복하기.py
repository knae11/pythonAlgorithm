def solution(s):
    convert = 0
    removed = 0
    while s != "1":
        convert += 1
        removed += s.count("0")
        s = s.replace("0", "")
        length = len(s)
        s = bin(length)[2:]
    return [convert, removed]


print(solution("110010101001"))
