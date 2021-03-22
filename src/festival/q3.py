#fail

import sys

length = int(sys.stdin.readline())
graph = []
for _ in range(length):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

count = [0 for _ in range(length + 1)]


def check_possible(i, j, n):
    if i + n > length or j + n > length:
        return False
    for a in range(i, i + n):
        for b in range(j, j + n):
            if graph[a][b] == 1:
                continue
            else:
                return False
    return True


def check_box(n):
    count = 0
    for i in range(length):
        for j in range(length):
            if check_possible(i, j, n):
                count += 1
    return count


for i in range(1, length + 1):
    count[i] = check_box(i)

print("total: " + str(sum(count)))
for number in range(1, len(count) + 1):
    if count[number] == 0:
        break
    print("size[" + str(number) + "]: " + str(count[number]))
