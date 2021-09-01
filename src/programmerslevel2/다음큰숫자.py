# 인터넷 풀이 참고! (예전에 풀었던 건데 방향을 잘못 택했다ㅠㅠㅠ)
# 1의 갯수만 세면 되는 것이었음!!!

def solution(n):
    answer = n
    bin_num = bin(n)[2:]
    ones = bin_num.count("1")
    while True:
        answer += 1
        if bin(answer).count("1") == ones:
            return answer


print(solution(78))
