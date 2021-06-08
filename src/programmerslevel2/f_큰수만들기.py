def solution(number, k):
    answer = ""
    # 초기값 셋팅
    remained_length = len(number)
    count = len(number) - k
    numbers = list(number)
    for i in range(len(number)):
        if remained_length - count <= 0:
            break
        if count <= 0:
            return answer
        f_list = numbers[:remained_length - count + 1]
        max_value = max(f_list)
        f_index = f_list.index(max_value)
        answer += str(max_value)
        numbers = numbers[f_index + 1:]
        remained_length = len(numbers)
        count -= 1
        # print(remained_length, count, f_index, answer, f_list)
    answer += "".join(numbers)

    return answer


print(solution("4177252841", 4))
