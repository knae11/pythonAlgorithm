# 2차원 배열 행, 열 뒤집기

arrays = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flip_arrays = list(map(list, zip(*arrays)))

print(arrays)
print(flip_arrays)

for item in zip(*arrays):
    print(item)
