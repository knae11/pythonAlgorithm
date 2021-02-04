def solution(participant, completion):
    answer = ''
    racer = dict()
    for parti in participant:
        racer[parti] = racer.get(parti, 0) + 1
    for compl in completion:
        racer[compl] -= 1
    for parti in participant:
        if racer[parti] != 0:
            return parti
    return answer


print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))


# 다른풀이 - Counter 사용!
'''
import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
'''
