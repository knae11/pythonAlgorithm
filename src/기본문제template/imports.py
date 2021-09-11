# from collections import deque
# import heapq

# 순열, 조합,
# from itertools import combinations # 순서없음
# from itertools import permutations # 순서있음
# from itertools import product # 2개이상의 리스트?!

# 복사
# from copy import deepcopy

# 이진탐색
# from bisect import bisect_right, bisect_left

test1 = [2, 6, 64, 7]
test1.reverse()  # 단순히 거꾸로 출력
test1.sort(reverse=True)  # 역정렬
print(test1)

test2 = sorted(test1, reverse=True)  # 역정렬
test3 = reversed(test1)  # 순서 뒤집기

text1 = ["10", "3", "200"]
text1.sort()
print(text1)  # [10, 200, 3] 앞자리 부터 문자열 크기대로 정렬됨

text_test1 = ["ac", "abc", "b"]
print(sorted(text_test1))  # ['abc', 'ac', 'b'] 길이 상관없이 앞에서 부터 정렬됨
print(sorted(text_test1, reverse=True))  # ['b', 'ac', 'abc']
