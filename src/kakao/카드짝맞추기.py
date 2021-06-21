from collections import deque
from copy import deepcopy
from itertools import permutations

n_board = []


def find_character(board):
    items = dict()
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                items[board[i][j]] = []
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                items[board[i][j]].append((i, j))
    return items


def ctrl_move(r, c, m_r, m_c):
    global n_board
    curr_r, curr_c = r, c
    while True:
        n_r = curr_r + m_r
        n_c = curr_c + m_c
        if not (0 <= n_c < 4 and 0 <= n_r < 4):
            return curr_r, curr_c
        if n_board[n_r][n_c] != 0:
            return n_r, n_c
        curr_c = n_c
        curr_r = n_r

# 다익스트라로 해야하는 거 아닌지?!!
def bfs(start, target):
    r, c = start
    t_r, t_c = target
    queue = deque()
    queue.append((r, c, 0))
    visited = [[False] * 4 for _ in range(4)]
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while queue:
        r, c, count = queue.popleft()
        if visited[r][c]:
            continue
        visited[r][c] = True
        if r == t_r and c == t_c:
            return count
        for m_r, m_c in move:
            curr_r = r + m_r
            curr_c = c + m_c
            if 0 <= curr_c < 4 and 0 <= curr_r < 4:
                queue.append((curr_r, curr_c, count + 1))
            curr_r, curr_c = ctrl_move(r, c, m_r, m_c)
            queue.append((curr_r, curr_c, count + 1))
    return 0


def solution(board, r, c):
    global n_board
    answer = 1e9
    nums = find_character(board)
    for combi in permutations(nums.keys(), len(nums)):
        count = 0
        n_board = deepcopy(board)
        s_r, s_c = r, c
        for i in combi:
            left = bfs((s_r, s_c), nums[i][0])
            right = bfs((s_r, s_c), nums[i][1])

            if left < right:
                count += left
                count += bfs(nums[i][0], nums[i][1])
                s_r, s_c = nums[i][1]
            else:
                count += right
                count += bfs(nums[i][1], nums[i][0])
                s_r, s_c = nums[i][0]

            n_board[nums[i][0][0]][nums[i][0][1]] = 0
            n_board[nums[i][1][0]][nums[i][1][1]] = 0
        answer = min(answer, count)
    answer += len(nums) * 2
    return answer


print(solution([[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]], 0, 1))
