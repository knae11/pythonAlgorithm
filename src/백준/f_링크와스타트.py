# todo: solving dfs

import sys
from itertools import combinations

n = int(sys.stdin.readline().rstrip())
graph = []
for i in range(n):
    line = list(map(int, sys.stdin.readline().rstrip().split()))
    graph.append(line)

members = [i for i in range(n)]

answer = 1e9


def calculate_score(given_list):
    score = 0
    for a in given_list:
        for b in given_list:
            score += graph[a][b]
    return score


for i in range(2, n - 1):
    for team in combinations(members, i):
        print(team)
        a_score = calculate_score(list(team))
        b_score = calculate_score(list(set(members) - set(team)))

        answer = min(abs(a_score - b_score), answer)
        if answer == 0:
            break
print(answer)
'''

answer = 1e9
for i in range(2, n):
    for team in combinations(members, i):
        team_a = list(team)
        team_b = list(set(members) - set(team))
        a_score = 0
        b_score = 0

        for i in team_a:
            for j in team_a:
                a_score += graph[i][j]

        for i in team_b:
            for j in team_b:
                b_score += graph[i][j]

        answer = min(abs(a_score - b_score), answer)

print(answer)


'''
