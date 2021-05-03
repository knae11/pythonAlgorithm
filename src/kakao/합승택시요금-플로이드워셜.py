# 스터디 이후 재도전 : 플로이드 워셜

def solution(n, s, a, b, fares):
    answer = 1e9
    # 최장거리를 기본을 셋팅
    graph = [[1e9] * (n + 1) for _ in range(n + 1)]
    # 자기자신은 가는비용이 0
    for i in range(n + 1):
        graph[i][i] = 0
    # i->j로 가는 기본 비용 셋팅 (양쪽다 셋팅해줌)
    for fare in fares:
        graph[fare[0]][fare[1]] = fare[2]
        graph[fare[1]][fare[0]] = fare[2]

    # 플로이드 워셜로 최단거리 셋팅
    for k in range(1, n + 1):  # 거치는 점
        for i in range(1, n + 1):  # 시작점
            for j in range(1, n + 1):  # 끝점
                # 1개의 케이스가 시간초과가 나서 min으로 업데이트가 아닌 조건문으로 처리해주니 통과
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    # (기존 정답 처리된 최단거리, 각각 가는 경우, 거쳐가는 경우) 중 가장 작은 값을 답으로 선택!
    for k in range(1, n + 1):
        answer = min(answer, graph[s][a] + graph[s][b], graph[s][k] + graph[k][a] + graph[k][b])
    return answer


print(solution(6, 4, 6, 2,
               [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22],
                [1, 6, 25]]))
