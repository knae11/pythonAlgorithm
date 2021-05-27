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


print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
