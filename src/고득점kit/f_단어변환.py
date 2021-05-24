# todo: solving

from collections import deque


def find_next(source, candidate):
    count = 0
    index = 0
    for k in range(len(source)):
        if source[k] != candidate[k]:
            count += 1
            index = k
    if count == 1:
        return True, index
    else:
        return False, index


def solution(begin, target, words):
    answer = 0
    completed = [False for _ in range(len(begin))]
    if target not in words:
        return 0
    queue = deque(words)
    while queue:
        next = queue.popleft()
        ok, index = find_next(begin, next)
        if ok and not completed[index]:
            begin = next
            answer += 1
            print(next, next[index])
            if next[index] == target[index]:
                completed[index] = True
        if not ok:
            queue.append(next)
        if begin == target:
            return answer

    return answer


# hit 000 -> hot 0-0 -> dog 0-- -> log --- -> cog

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
