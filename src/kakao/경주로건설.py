import copy

answer = 10e9


def dfs(board, pos, n, visited):
    x, y = pos[0][0], pos[0][1]
    dir = pos[1]
    cost = pos[2]
    print(board, pos, visited)
    global answer
    if pos[0] == (n, n):
        answer = min(answer, pos[2] * 100)
        print(answer)
    direction = [0, 1, 2, 3]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        nd = direction[i]
        if board[nx][ny] == 0 and (nx, ny) not in visited:
            if nd % 2 == dir % 2:
                curr = ((nx, ny), dir, cost + 1)
            if nd % 2 != dir % 2:
                curr = ((nx, ny), nd, cost + 6)
            visited.append((nx, ny))
            dfs(board, curr, n, visited[:])


def solution(board):
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]
    start_s = ((1, 1), 1, 0)
    start_c = ((1, 1), 0, 0)
    dfs(copy.deepcopy(new_board), start_s, n, [(1, 1)])
    print("---")
    dfs(copy.deepcopy(new_board), start_c, n, [(1, 1)])
    return answer


print(solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))
