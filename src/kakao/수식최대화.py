from collections import deque
from itertools import permutations


def solution(expression):
    answer = 0
    operators = ['+', '-', '*']
    refined_expression = []
    refined_expression.append(expression[0])
    # 연산가능한 요소단위로 배열로 만들기
    for i in range(1, len(expression)):
        letter = expression[i]
        if letter not in operators:
            if refined_expression[-1] in operators:
                refined_expression.append(letter)
            else:
                refined_expression.append(refined_expression.pop() + letter)
        if letter in operators:
            refined_expression.append(letter)
    # 우선순위에 따라 계산하기
    for combi in permutations(operators, 3):
        copy = refined_expression.copy()
        process = []
        for operator in combi:
            queue = deque(copy)
            while queue:
                item = queue.popleft()
                if item != operator:
                    process.append(item)
                else:
                    last_number = process.pop()
                    next_number = queue.popleft()
                    calculated = eval(last_number + item + next_number)
                    process.append(str(calculated))
            copy = process.copy()
            process = []
        answer = max(answer, abs(int(copy[0])))

    return answer


print(solution("100-200*300-500+20"))


'''
옛날 풀이
from itertools import permutations

def solution(expression):
    answer = 0
    operators = ["+","-","*"]
    expList = [expression[0]]
    for i in range(1,len(expression)) :
        if expression[i] not in operators and expList[-1] not in operators:
            expList[-1] += expression[i]
            continue
        expList.append(expression[i])
    for priority in list(permutations(operators,3)):
        newExpList = expList[:]
        for operator in priority:
            while True:
                if operator in newExpList:
                    index = newExpList.index(operator)
                    calculated = eval(newExpList[index-1]+newExpList[index]+newExpList[index+1])
                    newExpList[index+1] = str(calculated)
                    del newExpList[index-1:index+1]
                else:
                    break
        answer = max(answer,abs(int(newExpList[0])))
    return answer
'''