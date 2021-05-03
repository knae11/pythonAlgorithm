# DP를 활용하는 풀이 - 답안 코드 참고ㅠㅠ
def solution(board):
    answer = 0
    if board[0][0] == 1:
        answer = 1
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] != 0:
                board[i][j] = min(board[i - 1][j], board[i - 1][j - 1], board[i][j - 1]) + 1
                answer = max(answer, board[i][j] ** 2)

    return answer
