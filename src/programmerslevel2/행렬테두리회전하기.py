# 즉, 아무 회전도 하지 않았을 때, i 행 j 열에 있는 숫자는 ((i-1) x columns + j)입니다.
def solution(rows, columns, queries):
    answer = []
    # set board
    board = [[0 for _ in range(columns + 1)] for _ in range(rows + 1)]
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            board[i][j] = ((i - 1) * columns + j)
    for query in queries:
        start = (query[0], query[1])
        end = (query[2], query[3])
        points = get_points(start, end)
        moves = get_moves(board, points)
        answer.append(min(moves))
        move_board(moves, board, points)
    return answer


def get_points(start, end):
    points = []
    row = 0
    col = 1
    for i in range(start[col], end[col]):
        points.append((start[row], i))
    for i in range(start[row], end[row]):
        points.append((i, end[col]))
    for i in range(end[col], start[col], -1):
        points.append((end[row], i))
    for i in range(end[row], start[row], -1):
        points.append((i, start[col]))
    return points


def get_moves(board, points):
    moves = [1e9]
    for point in points:
        moves.append(board[point[0]][point[1]])
    moves[0] = moves[-1]
    return moves[:-1]


def move_board(moves, board, points):
    for n in range(len(moves)):
        number = moves[n]
        point = points[n]
        row = point[0]
        col = point[1]
        board[row][col] = number


print(solution(100, 97, [[1, 1, 100, 97]]))
