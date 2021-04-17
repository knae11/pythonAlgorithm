import copy
from collections import deque


def check_removable(i, j, origin_board, process_board):
    if origin_board[i][j] != "0" and origin_board[i + 1][j] == origin_board[i][j + 1] == origin_board[i + 1][j + 1] == \
            origin_board[i][j]:
        process_board[i][j] = "#"
        process_board[i + 1][j] = "#"
        process_board[i][j + 1] = "#"
        process_board[i + 1][j + 1] = "#"
        return process_board
    return process_board


def remove_items(process_board, m, n):
    new_board = [[] for _ in range(m)]
    count = 0
    for column in range(n):
        line = [process_board[row][column] for row in range(m)]
        new_line = deque([])
        for item in line:
            if item == "#":
                count += 1
            else:
                new_line.append(item)
        while len(new_line) < m:
            new_line.appendleft("0")
        for i in range(m):
            new_board[i].append(new_line[i])
    return new_board, count


def solution(m, n, board):
    answer = 0
    origin_board = [list(row) for row in board]

    while True:
        # 삭제할 아이템 확인하기
        process_board = copy.deepcopy(origin_board)
        for i in range(m):
            for j in range(n):
                if i == m - 1 or j == n - 1:
                    continue
                process_board = check_removable(i, j, origin_board, process_board)
        # 삭제하기
        origin_board, result_answer = remove_items(process_board, m, n)
        if result_answer == 0:
            return answer
        answer += result_answer


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))

# 이전 풀이를 참고하여 품
# https://programmers.co.kr/learn/courses/30/lessons/17679

'''
이전풀이

import copy
from collections import deque
def searchRemove(m,n,board):
    process=copy.deepcopy(board)
    for i in range(m-1):
        for j in range(n-1):
            if board[i][j] != " " and board[i][j] == board[i+1][j] and board[i][j] == board[i+1][j+1] and board[i][j] == board[i][j+1]:
                process[i][j]="#"
                process[i+1][j]="#"
                process[i][j+1]="#"
                process[i+1][j+1]="#"
    return process
def down(m,n,process, answer):
    for j in range(n):
        queue = deque()
        for i in range(m-1,-1,-1):
            if process[i][j] == "#":
                answer+=1
            else:
                queue.append(process[i][j])
        if len(queue) == m:
            continue
        for i in range(m-1,-1,-1):
            if queue:
                process[i][j] = queue.popleft()
            else:
                process[i][j] = " "
    return process, answer

def solution(m, n, board):
    answer = 0
    board=[list(line) for line in board]
    while True:
        process = searchRemove(m,n,board)
        board, answer1 = down(m,n,process,answer)
        if answer == answer1 :
            return answer
        answer = answer1
    return answer
'''
