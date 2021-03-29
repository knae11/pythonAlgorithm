from itertools import combinations

def solution(relation):
    column = len(relation[0])
    row = len(relation)
    indexes = [i for i in range(column)]
    candidates = []
    # 유일성을 만족하는 목록들
    for number in range(column+1):
        for combi in combinations(indexes, number):
            process = set()
            for item in relation:
                element = tuple([item[i] for i in combi])
                process.add(element)
                # 최소성까지 만족
                if len(process) == row and not any(set(candidate).issubset(set(combi)) for candidate in candidates):
                    candidates.append(combi)
    return len(candidates)


print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
                ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))

'''
기존버전
from itertools import combinations

def solution(relation):
    answer = 0
    columns = [ i for i in range(len(relation[0]))]
    combi = 1
    answerElements = []
    while True:
        if len(columns) < combi:
            break
        combiColumns = set(combinations(columns,combi))
        toBeDeleted = set()
        for candidate in combiColumns:
            for element in answerElements:
                if set(element).issubset(set(candidate)):
                    toBeDeleted.add(candidate)
        for column in combiColumns - toBeDeleted:
            key=set()
            for row in relation:
                candidates = tuple([row[i] for i in column])
                if candidates in key:
                    break
                key.add(candidates)
            else:
                answer+=1
                answerElements.append(column)
        combi+=1
    return answer
'''