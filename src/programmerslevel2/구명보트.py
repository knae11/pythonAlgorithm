from collections import deque

def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    persons = deque(people)
    min = persons[-1]
    while persons:
        max = persons.popleft()
        if max + min <= limit:
            if len(persons) >= 2:
                persons.pop()
                min = persons[-1]
            elif len(persons) == 1:
                persons.pop()
            answer += 1
        else:
            answer += 1

    return answer

print(solution([70, 50, 80, 50]	,100))