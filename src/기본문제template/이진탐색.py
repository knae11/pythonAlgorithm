# 이것이 취업을 위한 코딩테스트다(나동빈)

# 재귀로 구현한 이진탐색
def binary_search_recursive(array, target, start, end):
    if start > end:
        return None
    # 반으로 쪼개 탐색
    mid = (start + end) // 2
    # 재귀니까 종료 조건✨
    # 값을 찾으면 종료
    if array[mid] == target:
        return mid
    # 중간점보다 찾는 값이 작은 경우, start~mid-1 탐색
    if array[mid] > target:
        return binary_search_recursive(array, target, start, mid - 1)
    # 중간점보다 찾는 값이 큰 경우, mid+1~start 탐색
    if array[mid] < target:
        return binary_search_recursive(array, target, mid + 1, start)


# 반복문으로 구현한 이진탐색
def binary_search_while(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 값을 찾은 경우 종료✨
        if array[mid] == target:
            return mid
        if array[mid] > target:
            end = mid - 1
        if array[mid] < target:
            start = mid + 1
    return None


'''
원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제 : 파라메트릭 서치
구현은 보통 이진탐색을 사용하여 해결한다.
'''
