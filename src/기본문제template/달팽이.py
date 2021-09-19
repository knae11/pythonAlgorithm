def dalphang(n):
    result = []
    for y in range(0, n):
        line = []
        for x in range(0, n):
            p = min(x, y, n - x - 1, n - y - 1)
            if x >= y:
                q = x + y - 2 * p
            else:
                q = (n - 1 - 2 * p) * 4 - (x + y - 2 * p)
            q += 4 * (p * n - (p * p))
            line.append(q)
            print("{:3d}".format(q), end="")
        result.append(line)
        print()
    return result


print(dalphang(4))


def dalphang2(n):
    value = 1
    move = 1
    row, col = 0, -1
    result = [[0] * n for _ in range(n)]
    while n > 0:
        for i in range(n):
            col += move
            result[row][col] = value
            value += 1
        n -= 1
        for i in range(n):
            row += move
            result[row][col] = value
            value += 1
        # 곱하기로 -1, 1 변화
        move *= -1
    for line in result:
        print(line)
    return result


print("dalphang", dalphang2(5))
