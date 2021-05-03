# 인터넷 풀이 참고함.ㅠㅠㅠ

answer = 0
def dfs(numbers, target, process, index):
    global answer
    if len(process) >= len(numbers):
        if sum(process) == target:
            answer += 1
            return
        else:
            return
    plus = process + [numbers[index]]
    minus = process + [-numbers[index]]
    dfs(numbers, target, plus, index+1)
    dfs(numbers, target, minus, index+1)

def solution(numbers, target):
    dfs(numbers, target, [], 0)
    return answer

print(solution([1, 1, 1, 1, 1], 3))
