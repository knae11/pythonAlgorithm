def solution(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    k = len(arr2[0])
    answer = [[] for _ in range(m)]
    for a in range(m):
        for c in range(k):
            result = 0
            for b in range(n):
                result += arr1[a][b] * arr2[b][c]
            answer[a].append(result)
    return answer


print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
