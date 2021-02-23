# 플로이드 워셜 알고리즘
'''
모든 지점에서 다른 모든 지점까지의 최단경로를 모두 구해야 하는 경우
점화식에 맞게 매번 2차원 배열의 값(최소비용)을 갱신함
아래 예시는 전체 로직보다는 핵심 로직(+컴파일이 되기 위한 코드)만 작성함.
'''
a, b, c, n = 0, 0, 0
INF = 1e9

graph = [[INF] * (n + 1) for _ in range(n + 1)] # 거리 정보를 가질 2차원 그래프!

# for문을 돌면서 초기화 시켜줌
graph[a][b] = c  # a에서 b로 가는 비용 : c

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            # a->b 경우에서 k를 거쳐가는 것과 비교해서 최소 값으로 갱신
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
