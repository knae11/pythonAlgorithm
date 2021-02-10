import copy


def dfs(board, pos, n):
    print(board, pos)
    x, y = pos[0][0], pos[0][1]
    prev = pos[1]
    cost = pos[2]
    board[x][y] = 1
    if pos[0] == (n, n):
        print(pos)
        return pos
    dx_s = [0, 0]
    dy_s = [1, -1]
    dx_c = [1, -1]
    dy_c = [0, 0]
    # 가로
    if prev == 0:
        # 가로 가능
        for i in range(2):
            nx = x + dx_s[i]
            ny = y + dy_s[i]
            if board[nx][ny] == 0:
                curr = ((nx, ny), 0, cost + 1)
                dfs(board, curr, n)
        # 세로
        for i in range(2):
            nx = x + dx_c[i]
            ny = y + dy_c[i]
            if board[nx][ny] == 0:
                curr = ((nx, ny), 1, cost + 6)
                dfs(board, curr, n)
    # 세로
    else:
        # 세로
        for i in range(2):
            nx = x + dx_c[i]
            ny = y + dy_c[i]
            if board[nx][ny] == 0:
                curr = ((nx, ny), 1, cost + 1)
                dfs(board, curr, n)
        # 가로
        for i in range(2):
            nx = x + dx_s[i]
            ny = y + dy_s[i]
            if board[nx][ny] == 0:
                curr = ((nx, ny), 0, cost + 6)
                dfs(board, curr, n)


def solution(board):
    answer = 0
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]
    start_c = ((1, 1), 1, 0)
    start_s = ((1, 1), 0, 0)
    s_result = dfs(copy.deepcopy(new_board), start_s, n)
    print("-----------")
    c_result = dfs(copy.deepcopy(new_board), start_c, n)
    print(s_result, c_result)
    return 0


print(solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))
