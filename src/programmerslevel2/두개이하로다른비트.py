# 인터넷 풀이 참고
# 규칙을 찾아야 하는 문제였다. (이진수 변환의 경우, 1. 하라는 대로 한다. 2. 규칙을 찾는다 3. 시프트 연산이용한다.)
def solution(numbers):
    answer = []
    for number in numbers:
        if number % 2 == 0:
            answer.append(number + 1)
        else:
            b_n = "0" + bin(number)[2:]
            index = b_n.rfind("0")
            result = list(b_n)
            result[index] = "1"
            result[index + 1] = "0"
            answer.append(int("".join(result), 2))
    return answer


print(solution([2, 7]))
