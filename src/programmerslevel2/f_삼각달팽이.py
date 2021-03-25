def solution(n):
    answer = []
    process = [[0] for _ in range(n)]
    print(process)
    up = 1
    down = n - 1
    max = n * (n + 1) / 2
    number = 1

    i = 0
    while (number <= max):
        process[i].insert(-1,number)
        number += 1
        i += 1
        if i == down:
            down -= 1
            for _ in range(i+1):
                if number > max:
                    break
                process[i].insert(-1,number)
                number += 1

            for k in range(i-1, -1, -1):
                print("1",k, up)
                if number > max:
                    break
                if k == up:
                    i = k
                    up += 1
                    break
                process[k].insert(-1,number)
                print("add", i, number)
                number += 1

    print(process)

    for row in range(n):
        process[row].pop()
        answer += process[row]
    return answer


print(solution(4))
