from collections import deque

COST = 2


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def dijkstra(n, s, a, b, spanning_tree):
    cost = 0
    q = deque(spanning_tree[s])
    visited = [False for _ in range(n+1)]
    visited[s] = True
    while q:
        dist, now = q.popleft()
        if visited[a] and visited[b]:
            return cost
        if visited[now]:
            continue
        visited[now] = True
        cost += dist
        for i in spanning_tree[now]:
            q.append(i)
        spanning_tree[now].clear()


def solution(n, s, a, b, fares):
    answer = 0
    parent = [0] * (n + 1)
    for i in range(1, n + 1):
        parent[i] = i
    edges = []
    for fare in fares:
        edges.append((fare[COST], fare[0], fare[1]))
    edges.sort()
    spanning_tree = [[] for _ in range(n + 1)]
    for edge in edges:
        cost, x, y = edge
        if find_parent(parent, x) != find_parent(parent, y):
            union_parent(parent, x, y)
            spanning_tree[x].append((cost, y))
            spanning_tree[y].append((cost, x))

    return dijkstra(n, s, a, b, spanning_tree)


print(solution(6, 4, 6, 2,
               [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22],
                [1, 6, 25]]))
