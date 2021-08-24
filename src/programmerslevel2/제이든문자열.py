def solution(s):
    answer = ''
    process = ''
    s += " "
    for letter in s:
        if letter == " ":
            converted = process.capitalize()
            answer += converted
            process = ''
            answer += " "
        else:
            process += letter
    return answer[:-1]

print(solution("3people unFollowed me"))