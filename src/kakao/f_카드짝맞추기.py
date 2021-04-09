def find_target(board, target):
    for i in range(4):
        for j in range(4):
            if board[i][j] == target:
                return i, j


def is_new_target_on_same_line(board, r, c):
    for k in range(4):
        if board[r][k] != 0:
            return True
        if board[k][c] != 0:
            return True
    return False


def find_next_target(board, r, c):
    for k in range(4):
        if board[r][k] != 0:
            return board[r][k], r, k
        if board[k][c] != 0:
            return board[k][c], k, c
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                return board[i][j], i, j

def is_cards_left(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] !=0:
                return True
    return False

def mark_target(r, c, target_r, target_c):
    if target_r == r or target_c == c:
        return 1
    else:
        return 2

def solution(board, r, c):
    answer = 0
    # Enter 의 갯수
    characters = set()
    for line in board:
        for item in line:
            if item != 0:
                characters.add(item)
    answer += len(characters) * 2

    current_r = r
    current_c = c
    # 움직임 갯수
    while is_cards_left(board):
        if board[current_r][current_c] != 0:
            target = board[current_r][current_c]
            answer, current_c, current_r = match_cards(answer, board, current_c, current_r, target)
        else:
            if is_new_target_on_same_line(board, current_r, current_c):
                answer += 1
                target, current_r, current_c = find_next_target(board, current_r, current_c)
                answer, current_c, current_r = match_cards(answer, board, current_c, current_r, target)
            # todo: 거리가 3인경우도 확인해야
            else:
                answer += 2
                target, current_r, current_c = find_next_target(board, current_r, current_c)
                answer, current_c, current_r = match_cards(answer, board, current_c, current_r, target)
    return answer


def match_cards(answer, board, current_c, current_r, target):
    board[current_r][current_c] = 0
    target_r, target_c = find_target(board, target)
    answer += mark_target(current_r, current_c, target_r, target_c)
    board[target_r][target_c] = 0
    current_r, current_c = target_r, target_c
    return answer, current_c, current_r




print(solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0))
