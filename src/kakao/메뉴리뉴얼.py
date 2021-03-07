from itertools import combinations

def solution(orders, course):
    answer = []
    menu_list = set()
    for order in orders:
        for menu in order:
            menu_list.add(menu)

    for r in course:
        candidates = []
        max_value = 0
        for combination in combinations(menu_list, r):
            menu = set(combination)
            count = 0
            for order in orders:
                order_menu = set(order)
                if menu.issubset(order_menu):
                    count += 1
            max_value = max(max_value, count)

            if count < 2 or count < max_value:
                continue
            menu_combi = "".join(sorted(menu))
            candidates.append((menu_combi, count))
        if not candidates:
            continue
        for candidate in sorted(candidates, key=lambda x : -x[1]):
            if candidate[1] != max_value:
                break
            answer.append(candidate[0])
    return sorted(answer)


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
