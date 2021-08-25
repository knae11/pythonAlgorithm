def solution(brown, yellow):
    answer = []
    divides = []
    for i in range(1, int(yellow ** 0.5) + 1):
        if yellow % i == 0:
            divides.append((i, yellow // i))
    for divide in divides:
        a,b = divide[0], divide[1]
        if (a+2)*(b+2) == brown+yellow:
            answer.append(b+2)
            answer.append(a+2)
            break

    return answer


print(solution(10, 2))
