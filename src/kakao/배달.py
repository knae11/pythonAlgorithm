import heapq

def solution(N, road, K):
    answer = 0
    INF = 1e9
    graph = [[] for _ in range(N + 1)]
    # 양방향 셋팅을 해주지 않으면 예상과 다른 결과가 나옴ㅠㅠ
    for conn in road:
        a = conn[0]
        b = conn[1]
        cost = conn[2]
        # 양방향 셋팅을 해주지 않으면 예상과 다른 결과가 나옴ㅠㅠ
        graph[a].append((b, cost))
        graph[b].append((a, cost))

    distance = [INF] * (N + 1)
    # 자기자신까지의 거리는 0으로 초기화해줘야 다 통과되었음;;
    distance[1] = 0
    q = []
    heapq.heappush(q, (0, 1))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    for result in distance:
        if result <= K:
            answer += 1
    return answer

print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))
