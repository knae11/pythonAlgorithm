import heapq


def solution(n, edge):
    answer = 0
    distances = [1e9] * (n + 1)
    # 초기 방문하지 않는 부분 + 1->1 은 0으로 셋팅
    distances[0] = 0
    distances[1] = 0
    graph = [[] for _ in range(n + 1)]
    for vertex in edge:
        graph[vertex[0]].append((vertex[1], 1))
        graph[vertex[1]].append((vertex[0], 1))
    q = []
    heapq.heappush(q, (0, 1))
    while q:
        dist, now = heapq.heappop(q)
        if distances[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distances[i[0]]:
                distances[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    max_dist = max(distances)
    for distance in distances:
        if distance == max_dist:
            answer += 1
    return answer

'''
# 다른풀이

def solution(n, edge):
    graph =[  [] for _ in range(n + 1) ]
    distances = [ 0 for _ in range(n) ]
    is_visit = [False for _ in range(n)]
    queue = [0]
    is_visit[0] = True
    # 연결방식대로 셋팅
    for (a, b) in edge:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    
    while queue:
        i = queue.pop(0)
        
        for j in graph[i]:
            # 방문하지 않은 경우만
            if is_visit[j] == False:
                # 방문처리
                is_visit[j] = True
                # 큐에 추가
                queue.append(j)
                # 거리값 갱신
                distances[j] = distances[i] + 1

    distances.sort(reverse=True)
    answer = distances.count(distances[0])

    return answer
'''


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
