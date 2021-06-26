from collections import deque


def solution(genres, plays):
    answer = []
    genres_count = {}
    genres_info = {}
    for i in range(len(genres)):
        genres_count[genres[i]] = genres_count.get(genres[i], 0) + plays[i]
        genres_info[genres[i]] = []
    for i in range(len(genres)):
        genres_info[genres[i]].append((plays[i], i))

    for key, value in sorted(genres_count.items(), key=lambda x: -x[1]):
        g_list = genres_info[key]
        g_list.sort(key=lambda x: (-x[0], x[1]))
        queue = deque(g_list)
        count = 0
        while queue:
            if count > 1:
                break
            answer.append(queue.popleft()[1])
            count += 1
    return answer


print(solution(["classic", "pop", "classic", "pop", "classic", "classic"],
               [400, 600, 150, 600, 500, 500]))
