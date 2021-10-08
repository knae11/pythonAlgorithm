def solution(sizes):
    width = 0
    height = 0
    for size in sizes:
        width = max(max(size), width)
        height = max(min(size), height)
    return int(width * height)

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
