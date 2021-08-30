def solution(word):
    answer = 0
    convert = {"A": 1, "E": 2, "I": 3, "O": 4, "U": 5}
    converted = ""
    for w in word:
        converted += str(convert[w])
    while len(converted) < 5:
        converted += "0"
    num = [0, 5 ** 4, 5 ** 3, 5 ** 2, 5 ** 1]
    for i in range(5):
        note = int(converted[i])
        number = 0
        for k in range(i + 1, 5):
            number += num[k]
        if note - 1 < 0:
            answer += 0
        else:
            answer += note + (note - 1) * number

    return answer


print(solution("AAA"))
