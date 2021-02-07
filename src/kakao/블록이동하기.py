from collections import deque

def next_position(robot, board):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    # robot의 set을 index 접근을 하기위해 list 형식으로 변환
    robot = list(robot)
    x_t, y_t = robot[0][0], robot[0][1]
    x_h, y_h = robot[1][0], robot[1][1]
    # 다음 로봇이 될 수 있는 후보군들 (내부 좌표 값은 set으로 넣기)
    next_robot = []
    # 일반 상하좌우
    for i in range(4):
        nx_t, ny_t, nx_h, ny_h = x_t + dx[i], y_t + dy[i], x_h + dx[i], y_h + dy[i]
        if board[nx_t][ny_t] == 0 and board[nx_h][ny_h] == 0:
            next_robot.append({(nx_t, ny_t), (nx_h, ny_h)})
    # 가로의 경우 회전
    if x_t == x_h:
        for i in [1, -1]:
            if board[x_t + i][y_t] == 0 and board[x_h + i][y_h] == 0:
                next_robot.append({(x_t, y_t), (x_t + i, y_t)})
                next_robot.append({(x_h, y_h), (x_h + i, y_h)})
    # 세로의 경우 회전
    if y_t == y_h:
        # 오른쪽
        for i in [1, -1]:
            if board[x_t][y_t + i] == 0 and board[x_h][y_h + i] == 0:
                next_robot.append({(x_t, y_t), (x_t, y_t + i)})
                next_robot.append({(x_h, y_h), (x_h, y_h + i)})
    return next_robot


def solution(board):
    n = len(board)
    board_bound = [[1] * (n + 2) for _ in range(n + 2)]
    # index range 처리를 위해 바깥을 1로 감싸줌
    for i in range(n):
        for j in range(n):
            board_bound[i + 1][j + 1] = board[i][j]
    queue = deque()
    # robot의 좌표를 set 형식으로 해주어야 함
    robot = {(1, 1), (1, 2)}
    visited = []
    visited.append(robot)
    queue.append((robot, 0))
    while queue:
        curr_robot, cost = queue.popleft()
        # (n,n)에 도달하면 cost를 출력!
        if (n, n) in curr_robot:
            return cost
        for next_pos in next_position(curr_robot, board_bound):
            if next_pos not in visited:
                queue.append((next_pos, cost + 1))
                visited.append(next_pos)
    return 0

# 혼자 몇시간 고민해도 안풀려서 결국 답지를 참고하여 작성함..ㅠㅠ

print(
    solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))
