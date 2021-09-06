from itertools import product


def solution(info, query):
    answer = []
    collector = {}
    languages = ["java", "cpp", "python", "-"]
    jobs = ["backend", "frontend", "-"]
    careers = ["junior", "senior", "-"]
    foods = ["chicken", "pizza", "-"]
    for combi in product(languages, jobs, careers, foods):
        collector.setdefault("".join(combi), [])
    for inf in info:
        lines = inf.split(" ")
        for k in product([lines[0], "-"], [lines[1], "-"], [lines[2], "-"],
                         [lines[3], "-"]):
            collector["".join(k)].append(int(lines[4]))
    for key in collector.keys():
        collector[key].sort()
    for q in query:
        targets = q.split(" and ")
        last_word = targets[3].split(" ")
        food, score = last_word[0], int(last_word[1])
        target = "".join([targets[0], targets[1], targets[2], food])
        score_list = collector[target]
        left, right = 0, len(score_list)
        while left < right:
            mid = (left + right) //2
            if score_list[mid] >= score:
                right = mid
            else:
                left = mid +1
        answer.append(len(score_list) - left)

    return answer


print(solution(
    ["java backend junior pizza 150", "python frontend senior chicken 210",
     "python frontend senior chicken 150", "cpp backend senior pizza 260",
     "java backend junior chicken 80", "python backend senior chicken 50"],
    ["java and backend and junior and pizza 100",
     "python and frontend and senior and chicken 200",
     "cpp and - and senior and pizza 250", "- and backend and senior and - 150",
     "- and - and - and chicken 100", "- and - and - and - 150"]))
