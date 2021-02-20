# 최단경로 알고리즘

# 리스트에 저장하여 갱신하는 특징이 있음

# 1. 다익스트라 알고리즘 : 한 개의 노드에서 모든 노드로 가는 최단거리

# 필요한 조기정보
n = 10
graph = [[] for _ in range(n + 1)]  # 연결정보 그래프(대부분 주어지는 것)
# 간선정보 graph를 [노드a].append( (노드b, cost) ) 로 셋팅함
visited = [[False] * range(n + 1)]  # 방문처리
distance = [1e9] * (n+1) # 최단거리를 무한으로 초기화


def get_smallest_node():
    min_value = 1e9
    index = 0
    for i in range(1, n+1):
        # 방문하지 않은 경우 중, min_value가 기존 distance 보다 작은 경우
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


# `한 노드`에서 모든 노드로 가는 각각의 최소비용을 계산
def dijkstra(start):
    # 시작 초기화
    distance[start] = 0
    visited[start] = True

    for j in graph[start]:
        distance[j[0]] = j[1]
    # start 노드와 연결된 노드의 그래프는 본인이 가지고 있는 cost로 초기화 (바로가는 경우의 비용)

    # 시작노드를 제외한 나머지 진행
    for _ in range(n-1):
        now = get_smallest_node() # 연결된 노드 중 방문하지 않은 비용이 가장 짧은 노드를 구함
        visited[now] =True

        # 현재 노드와 연결된 다른 노드를 가능 비용 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # distance[now] : 시작노드에서 연결된 노드 중 비용이 최소인 노드로 가는 비용
            # j[1] 최소비용에서 연결된 노드에 가는 비용
            if cost < distance[j[0]]: # 바로 연결노드로 가는 것보다 거쳐가는게 작은 경우
                distance[j[0]] = cost # 최소비용으로 갱신


# 2. 다익스트라 우선순위큐로 성능좋게 해결하기
import heapq

# 필요한 초기정보
m = 10
graph_2 = [[] for _ in range(m + 1)]  # 연결정보 그래프(대부분 주어지는 것)
# 간선정보 graph를 [노드a].append( (노드b, cost) ) 로 셋팅함
distance_2 = [10e9] * (n+1) # 최단거리를 무한으로 초기화

def dijkstra_priorityQueue(start):
    q = []
    heapq.heappush(q, (0, start)) # 처음에 대상 q에 (cost, 출발노드)를 넣어줌
    distance_2[start] = 0
    while q: # q에 있는 동안 진행
        dist, now = heapq.heappop(q)
        # 가지고 있는 cost 보다 distance_2의 정보가 작을 때 -> 처리된 경우
        if distance_2[now] < dist :
            continue
        # 현재노드와 인접한 노드 확인 (기준이 계속 start 노드가 되는 것이 아니고 q에서 뽑힌게 현재노드임)
        for i in graph_2[now]:
            # 현재노드를 거쳐 다른 노드로 가능 경우
            cost = dist + i[1]
            # 본인이 가지고 있는 거리정보보다 최소인 경우
            if cost < distance_2[i[0]]:
                # 본인이 가진 거리정보 최소화함
                distance_2[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

