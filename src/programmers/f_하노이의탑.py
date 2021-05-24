# todo:바꾸는 방법은???ㅠㅠㅠ

def firstMove(s, e):
    return [[s, e]]


def twoMove(s, e, tmp):
    return [[s, tmp], [s, e], [tmp, e]]


def threeMove(s, e, tmp):
    return twoMove(s, tmp, e) + firstMove(s, e) + twoMove(tmp, e, s)


def fourMove(s, e, tmp):
    return threeMove(s, tmp, e) + firstMove(s, e) + threeMove(tmp, e, s)


def fiveMove(s, e, tmp):
    return fourMove(s, tmp, e) + firstMove(s, e) + fourMove(tmp, e, s)


def six(s, e, tmp):
    return firstMove(s, tmp, e) + firstMove(s, e) + fiveMove(tmp, e, s)


def seven(s, e, tmp):
    return six(s, tmp, e) + firstMove(s, e) + six(tmp, e, s)


def eight(s, e, tmp):
    return seven(s, tmp, e) + firstMove(s, e) + seven(tmp, e, s)


def nine(s, e, tmp):
    return eight(s, tmp, e) + firstMove(s, e) + eight(tmp, e, s)


def ten(s, e, tmp):
    return nine(s, tmp, e) + firstMove(s, e) + nine(tmp, e, s)


def elev(s, e, tmp):
    return ten(s, tmp, e) + firstMove(s, e) + ten(tmp, e, s)


def twelv(s, e, tmp):
    return elev(s, tmp, e) + firstMove(s, e) + elev(tmp, e, s)


def thirt(s, e, tmp):
    return twelv(s, tmp, e) + firstMove(s, e) + twelv(tmp, e, s)


def fourti(s, e, tmp):
    return thirt(s, tmp, e) + firstMove(s, e) + thirt(tmp, e, s)


def fifth(s, e, tmp):
    return fourti(s, tmp, e) + firstMove(s, e) + fourti(tmp, e, s)


def solution(n):
    answer = []
    if n == 1:
        return firstMove(1, 3)
    if n == 2:
        return twoMove(1, 3, 2)
    if n == 3:
        return threeMove(1, 3, 2)
    if n == 4:
        return fourMove(1, 3, 2)
    if n == 5:
        return fiveMove(1, 3, 2)
    if n == 6:
        return six(1, 3, 2)
    if n == 7:
        return seven(1, 3, 2)
    if n == 8:
        return eight(1, 3, 2)
    if n == 9:
        return nine(1, 3, 2)
    if n == 10:
        return ten(1, 3, 2)
    if n == 11:
        return elev(1, 3, 2)
    if n == 12:
        return twelv(1, 3, 2)
    if n == 13:
        return thirt(1, 3, 2)
    if n == 14:
        return fourti(1, 3, 2)
    if n == 15:
        return fifth(1, 3, 2)
    return 0


print(solution(4) == fourMove(1, 3, 2))
