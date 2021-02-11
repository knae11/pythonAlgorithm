import copy

answer = 10e9


def dfs(board, pos, n, cost_board):
    x, y = pos[0][0], pos[0][1]
    dir = pos[1]
    cost = pos[2]
    global answer
    if pos[0] == (n, n):
        answer = min(answer, pos[2] * 100)
        return
    if cost > answer:
        return
    if cost_board[x][y] < cost:
        return
    direction = [0, 1, 2, 3]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        nd = direction[i]
        if board[nx][ny] == 0 and cost_board[nx][ny] >= cost:
            if nd % 2 == dir % 2:
                curr = ((nx, ny), dir, cost + 1)
                cost_board[nx][ny] = cost + 1
            if nd % 2 != dir % 2:
                curr = ((nx, ny), nd, cost + 6)
                cost_board[nx][ny] = cost + 6
            dfs(board, curr, n, cost_board)


def solution(board):
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]
    start_s = ((1, 1), 1, 0)
    start_c = ((1, 1), 0, 0)
    cost_board = [[10e9] * (n + 2) for _ in range(n + 2)]
    dfs(new_board, start_s, n, cost_board)
    dfs(new_board, start_c, n, cost_board)
    return answer


print(solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))
