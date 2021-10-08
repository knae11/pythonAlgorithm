def solution(triangle):
    answer = 0
    height = len(triangle)
    width = len(triangle[-1])
    dp = [[0] * width for _ in range(1, height + 1)]
    dp[0][0] = triangle[0][0]
    for i in range(height):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j] + triangle[i][j])
            else:
                dp[i][j] = max(dp[i][j], dp[i - 1][j] + triangle[i][j],
                               dp[i - 1][j - 1] + triangle[i][j])
    return max(dp[-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
