# 미로탈출 예제

from collections import deque

n = 5  # 임의값으로 일단 설정 (graph 크기가 되겠지)
graph = []  # 셋팅해줘야함

# 이동방향 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    # 큐 사용을 위한 deque 구현
    queue = deque()
    # 처음 값을 넣어줌
    queue.append((x, y))

    # 큐가 빌때까지 계속진행!
    while (queue):
        x, y = queue.popleft()
        # 상하좌우 이동하며 queue에 다음 값을 넣어줌
        for i in range(4):
            # 이동할 새로운 x,y값
            nx = x + dx[i]
            ny = y + dy[i]
            # 인덱스 벗어나는 것 무시 (인덱스 처리는 밖을 못가는 값으로 한 단계 더 감싼 새로운 그래프로 대체가능)
            if nx < 0 or ny < 0 or nx >= n or ny >= 0:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 갈 수 있는 경우 & 처음 방문하는 경우
            if graph[nx][ny] == 1:
                # 최단거리 기록 (기존값 +1)
                graph[nx][ny] = graph[x][y] + 1
                # 이어서 더 진행해야하니 queue에 넣어줌
                queue.append((nx, ny))
    return graph[n - 1][n - 1]  # 가장 끝의 값을 부르면 최단 거리가 됨
