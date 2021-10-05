'''
- 여기서 return 조건을 잘 못 주었을때, 실패함..
- dfs 의 핵심은 재귀!
- 재귀의 핵심은 종료조건!
'''


def dfs(i, computers, n, visited):
    visited[i] = True
    for j in range(n):
        if computers[i][j] == 1 and not visited[j]:
            dfs(j, computers, n, visited)


def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for i in range(n):
        if not visited[i]:
            dfs(i, computers, n, visited)
            answer += 1
    return answer
