from itertools import combinations


def solution(orders, course):
    answer = []
    menu_list = dict()
    for order in orders:
        for i in range(1, len(order) + 1):
            for menu in combinations(order, i):
                key = ''.join(map(str, sorted(menu)))
                menu_list[key] = menu_list.get(key, 0) + 1
    for number in course:
        result = dict(filter(lambda x: len(x[0]) == number and x[1] > 1, menu_list.items()))
        if not result:
            continue
        max_value = max(result.values())
        candidates = list(filter(lambda x: x[1] == max_value, result.items()))
        for candidate in candidates:
            answer.append(candidate[0])
    return sorted(answer)


'''
# 다른풀이

import collections
import itertools

def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            # course_size 만큼 다 돌면서 combination, sorted() --> set 처럼 관리하기 위해! 메뉴 순서 상관 x
            # iterate 가능하게 만들어서 추가함. list 에 추가도 + 로 되다니...
            order_combinations += itertools.combinations(sorted(order), course_size)
        # list 를 Counter 해서 most_common()으로 list(tuple) 형태로 가져옴. tuple = (('x','y'), 2)
        most_ordered = collections.Counter(order_combinations).most_common()
        # 첫번째 가장 많은 수와 같은 것들 + 1회 초과하여 주문한 것들을 result 의 리스트로 가져옴
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]
        # result 의 배열을 정렬하고 ''.join 으로 문자열 형태로 변환하여 반환
    return [ ''.join(v) for v in sorted(result) ]
'''

print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
