from collections import defaultdict

def solution(clothes):
    answer = 1
    wearable = defaultdict(list)
    for cloth in clothes:
        item, theme = cloth[0], cloth[1]
        wearable[theme].append(item)
    for k, v in wearable.items():
        answer *= len(v)+1
    return answer - 1


print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"],
                ["green_turban", "headgear"]]))
