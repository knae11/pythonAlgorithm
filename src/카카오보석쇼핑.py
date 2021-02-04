def solution(gems):
    items = len(set(gems))
    shopping = dict()
    start = 0
    end = 0
    candidates = []
    for i in range(len(gems)):
        shopping[gems[i]] = shopping.get(gems[i], 0) + 1
        end = i
        if len(shopping) == items:
            for j in range(start, len(gems)):
                # start를 현재 j 값으로 셋팅하고
                start = j
                candidates.append((end - start, [start + 1, end + 1]))
                # 다음을 위해 다음 값으로 변경해줌
                start = j+1
                shopping[gems[j]] = shopping.get(gems[j]) - 1
                if shopping[gems[j]] == 0:
                    del (shopping[gems[j]])
                    break
    candidates.sort(key=lambda x: (x[0], x[1][0]))
    return candidates[0][1]


print(solution(["AA", "AB", "AC", "AA", "AC"]))
