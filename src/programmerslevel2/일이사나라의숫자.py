def solution(n):
    answer = ''
    nums = [ 1, 2, 4]
    while n > 0:
        n, re = divmod(n-1, 3)
        answer += str(nums[re])

    return answer[::-1]


print(solution(12))
