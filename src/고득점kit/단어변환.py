from collections import deque


def find_candidates(words, current):
    a_list = []
    length = len(current)
    for word in words:
        count = 0
        if word == current:
            continue
        for i in range(length):
            if word[i] != current[i]:
                count += 1
        if count == 1:
            a_list.append(word)
    return a_list


def solution(begin, target, words):
    queue = deque()
    queue.append((begin, 0))
    if target not in words:
        return 0
    while queue:
        current, cost = queue.popleft()
        if current == target:
            return cost
        candidates = find_candidates(words, current)
        for candidate in candidates:
            queue.append((candidate, cost + 1))

    return 0


# hit 000 -> hot 0-0 -> dog 0-- -> log --- -> cog

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
