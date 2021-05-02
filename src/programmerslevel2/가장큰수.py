# 다른사람 풀이 참고 : 숫자 문자열의 정렬! *앞자리*부터 단순 사전형 비교를 한다.
def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    # 1000까지의 수이므로 *3을하여 비교, 3 -> 333, 30 -> 303030 문자열 비교시 '333' > '303030'
    numbers.sort(key=lambda x: x * 3, reverse=True)
    # 0 때문에 int -> str 변환작업이 필요함
    return str(int(''.join(numbers)))


print(solution([3, 30, 34, 5, 9]))
