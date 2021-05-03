import re


def solution(s):
    answer = []
    # 전방탐색 (?=조건)
    # 후방탐색 (?<=조건)
    # 게으른수량자 +? 최소한의 것만 찾아줌 이거 안하면 {제외하고 시작한 '2},{2,1},{2,1,3},{2,1,3,4}' 이렇게 전체를 찾음
    parsed = re.compile("(?<={).+?(?=})")
    newS = list()
    for item in parsed.findall(s[1:]):
        newS.append(set(map(int, item.split(","))))
    newS = sorted(newS, key=lambda x: len(x))
    answer.append(newS[0].pop())
    for i in range(1, len(newS)):
        answer.append((newS[i] - set(answer)).pop())
    return answer


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
