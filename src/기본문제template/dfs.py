# 이것이 취업을 위한 코딩테스트다(나동빈) 음료수 얼려먹기 예제

graph = [] # 셋팅해줘야함
n = 5  # 임의값으로 일단 설정 (graph 크기가 되겠지)
result = 0


# 재귀로 구현할 것이므로 종료조건을 명시한다!
def dfs(x, y):
    # 주어진 범위 제외 종료처리 (인덱스 처리는 밖을 못가는 값으로 한 단계 더 감싼 새로운 그래프로 대체가능)
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    # 방문할 수 있는 경우
    if graph[x][y] == 0:
        # 방문처리
        graph[x][y] = 1
        # 상하좌우 dfs 호출
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            result += 1
