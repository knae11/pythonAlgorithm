# pass

import sys

weight = list(map(float, sys.stdin.readline().rstrip().split()))
weight_dict = {"A": weight[0],
               "B": weight[1],
               "C": weight[2],
               "D": weight[3],
               "E": weight[4]
               }
n, m = map(int, sys.stdin.readline().rstrip().split())
open_info = []
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    open_info.append([i for i in word])

gerne_info = []
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    gerne_info.append([i for i in word])

first = []
second = []
for i in range(n):
    for j in range(m):
        if open_info[i][j] == "Y":
            gerne = gerne_info[i][j]
            first.append((gerne, weight_dict.get(gerne), i, j))
        if open_info[i][j] == "O":
            gerne = gerne_info[i][j]
            second.append((gerne, weight_dict.get(gerne), i, j))
first.sort(key=lambda x: -x[1])
second.sort(key=lambda x: -x[1])

for item in first:
    print('{0} {1} {2} {3}'.format(item[0], item[1], item[2], item[3]))
for item in second:
    print('{0} {1} {2} {3}'.format(item[0], item[1], item[2], item[3]))