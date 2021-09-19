def comb(lst, n):
    ret = []
    if n > len(lst): return ret

    if n == 1:
        for i in lst:
            ret.append([i])
    elif n > 1:
        for i in range(len(lst) - n + 1):
            for temp in comb(lst[i + 1:], n - 1):
                ret.append([lst[i]] + temp)

    return ret


print("combination:", comb([1, 2, 3, 4], 2))


def perm(lst, n):
    ret = []
    if n > len(lst): return ret

    if n == 1:
        for i in lst:
            ret.append([i])
    elif n > 1:
        for i in range(len(lst)):
            temp = [i for i in lst]
            temp.remove(lst[i])
            for p in perm(temp, n - 1):
                ret.append([lst[i]] + p)

    return ret


print("permutation:", perm([1, 2, 3, 4], 2))


def dfs_comb(lst, n):
    ret = []
    idx = [i for i in range(len(lst))]

    stack = []
    print(len(lst) - n + 1, idx[:len(lst) - n + 1])
    for i in idx[:len(lst) - n + 1]:
        stack.append([i])

    while len(stack) != 0:
        cur = stack.pop()

        for i in range(cur[-1] + 1, len(lst) - n + 1 + len(cur)):
            temp = cur + [i]
            if len(temp) == n:
                element = []
                for i in temp:
                    element.append(lst[i])
                ret.append(element)
            else:
                stack.append(temp)
    return ret


print("dfs_combination:", dfs_comb([1, 2, 3, 4], 2))


def dfs_perm(lst, n):
    ret = []
    idx = [i for i in range(len(lst))]
    stack = []
    # stack에 모든 index를 리스트로 담아둔다.
    for i in idx:
        stack.append([i])

    # 모든 index 를 도는 동안
    while len(stack) != 0:
        cur = stack.pop()
        # 모든 index에 대해
        for i in idx:
            # 뽑은 index 가 아니라면 (중복 순열을 하고 싶다면 이부분 체크를 없애주면 됨)
            if i not in cur:
                # 임시로 만든 리스트에 i 를 넣음
                temp = cur + [i]
                # n 이라면
                if len(temp) == n:
                    # 해당 temp에 있던 index에 해당하는 원소를 list 에서 찾아 element로 만듦
                    element = []
                    for i in temp:
                        element.append(lst[i])
                    # 반환 리스트에 넣어줌
                    ret.append(element)
                # 아니라면 stack에 해당 내용을 넣어줌
                else:
                    stack.append(temp)
    return ret


print("dfs_permutation:", dfs_perm([1, 2, 3, 4], 2))


def bitmask_dfs_combination(list, number):
    result = []
    if number < 1:
        return result
    if number == 1:
        for item in list:
            result.append([item])
        return result

    stack = []
    idx = [i for i in range(len(list))]

    for i in idx:
        stack.append([i])
    while len(stack) != 0:
        current = stack.pop()
        for i in idx:
            if i not in current:
                temp = current + [i]
                if len(temp) == number:
                    element = []
                    for i in temp:
                        element.append(list[i])
                    result.append(element)
                else:
                    stack.append(temp)

    return result


print("bitmask_dfs_combination:", bitmask_dfs_combination([5, 6, 7, 8], 2))
