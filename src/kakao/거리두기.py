def check_distance(source, target, place):
    # i 확인
    si = source[0]
    sj = source[1]
    ti = target[0]
    tj = target[1]
    if ti > si:
        while ti - si > 0:
            if place[si][sj] == "O":
                return False
            si += 1
    else:
        while si - ti > 0:
            if place[si][sj] == "O":
                return False
            si -= 1
    if tj > sj:
        # j 확인
        while tj - sj > 0:
            if place[si][sj] == "O":
                return False
            sj += 1
    else:
        while sj - tj > 0:
            if place[si][sj] == "O":
                return False
            sj -= 1

    return True


dist_one = [(1, 0), (0, 1), (-1, 0), (0, -1)]
dist_two = [(1, 1), (2, 0), (0, 2), (-1, -1), (-2, 0), (0, -2), (1, -1),
            (-1, 1)]


def keep_distance(place):
    for i in range(5):
        for j in range(5):
            # 맨하튼 거리 1칸짜리
            for dist in dist_one:
                ni, nj = i + dist[0], j + dist[1]
                if ni > 4 or nj > 4 or ni < 0 or nj < 0:
                    continue
                if place[i][j] == "P" and place[ni][nj] == "P":
                    return False
            # 맨하튼 거리 2칸짜리
            for dist in dist_two:
                ni, nj = i + dist[0], j + dist[1]
                if ni > 4 or nj > 4 or ni < 0 or nj < 0:
                    continue
                if place[i][j] == "P" and place[ni][
                    nj] == "P" and not check_distance((i, j), (ni, nj),
                                                      place):
                    return False
    return True


def solution(places):
    answer = []
    for place in places:

        if not keep_distance(place):
            answer.append(0)
        else:
            answer.append(1)
    return answer


print(solution([["OOPOO", "OPOOO", "OOOOO", "OOOOO", "OOOOO"]]))
