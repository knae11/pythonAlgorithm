from itertools import chain


def divide(arr, start, end):
    result = []
    start_x, start_y = start[0], start[1]
    end_x, end_y = end[0], end[1]
    for i in range(start_x, end_x):
        line = []
        for j in range(start_y, end_y):
            line.append(arr[i][j])
        result.append(line)
    return result


def compressed(arr, answer):
    if len(arr) == 1:
        if sum(arr[0]) == 1:
            answer[1] += 1
        else:
            answer[0] += 1
        return
    n = len(arr)
    half = len(arr) // 2
    if sum(chain(*arr)) == n * n:
        answer[1] += 1
        return
    if sum(chain(*arr)) == 0:
        answer[0] += 1
        return
    one = divide(arr, (0, 0), (half, half))
    two = divide(arr, (0, half), (half, n))
    three = divide(arr, (half, 0), (n, half))
    four = divide(arr, (half, half), (n, n))
    compressed(one, answer)
    compressed(two, answer)
    compressed(three, answer)
    compressed(four, answer)
    return


def solution(arr):
    answer = [0, 0]
    compressed(arr, answer)
    return answer


print(solution([[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]))
