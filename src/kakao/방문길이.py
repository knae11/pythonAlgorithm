def solution(dirs):
    answer = 0
    lines = []

    x = 5
    y = 5

    direction = {"U": 0, "D": 1, "R": 2, "L": 3}

    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]

    for dir in dirs:
        index = direction[dir]

        nx = x + dx[index]
        ny = y + dy[index]
        if nx < 0 or ny < 0 or nx > 10 or ny > 10:
            continue
        if {(ny, nx), (y, x)} not in lines:
            answer += 1
            lines.append({(ny, nx), (y, x)})
        x = nx
        y = ny
    return answer


print(solution("ULURRDLLU"))

print(solution("LULLLLLLU"))
