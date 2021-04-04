from collections import deque
def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        queue = deque(skill)
        for letter in skill_tree:
            if letter in queue and letter != queue.popleft():
                break
        else:
            answer += 1
    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))

'''
예전풀이

import re
def solution(skill, skill_trees):
    answer = 0
    compareN =[i for i in range(len(skill))]
    for j in range(len(skill_trees)):
        for i in range(len(skill)):
            skill_trees[j] = skill_trees[j].replace(skill[i], "*"+ str(i))
        numbers = list(map(int,re.findall("\d+", skill_trees[j])))
        if(len(numbers) ==0 or (numbers[0] == 0 and compareN[:len(numbers)] == numbers)):
            answer+=1
    return answer
'''