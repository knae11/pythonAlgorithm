# 인터넷 검색 답안 참고 ㅠㅠㅠ
def solution(n):
    answer = []
    process = [[0] * n for _ in range(n)]
    x, y = -1, 0
    number = 1
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1
            process[x][y] = number
            number += 1

    for list in process:
        for item in list:
            if item == 0:
                break
            else:
                answer.append(item)
    return answer


print(solution(4))
