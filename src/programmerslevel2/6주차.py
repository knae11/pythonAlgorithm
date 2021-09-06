def solution(weights, head2head):
    answer = []
    n = len(weights)
    for i in range(n):
        board = head2head[i]
        wins = 0
        over_me = 0
        my = weights[i]
        num = i
        if board.count("N") == len(board):
            wins = 0
        else:
            wins = board.count("W") / (board.count("W") + board.count("L"))
        for j in range(n):
            if head2head[i][j] == "W" and weights[j] > weights[i]:
                over_me += 1
        answer.append((wins, over_me, my, num))
    answer.sort(key=lambda x: (-x[0], -x[1], -x[2], x[3]))
    print(answer)
    return [info[3] + 1 for info in answer]

print(solution([50,82,75,120],	["NLWL","WNLL","LWNW","WWLN"]))
