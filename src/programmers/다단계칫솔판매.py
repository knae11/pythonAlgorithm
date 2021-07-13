def ten_percent(money):
    return int(money / 10)


def solution(enroll, referral, seller, amount):
    answer = []
    outcomes = dict()
    trees = dict()
    for name in enroll:
        outcomes[name] = [0]

    for i in range(len(referral)):
        child = enroll[i]
        parent = referral[i]
        trees[child] = parent

    for i in range(len(seller)):
        earn = amount[i] * 100
        self = seller[i]
        outcomes[self].append(earn)
        if trees[self] == "-":
            outcome = ten_percent(earn)
            outcomes[self][-1] = (earn - outcome)
            continue
        while True:
            parent = trees[self]
            outcome = ten_percent(earn)
            outcomes[self][-1] = (earn - outcome)
            if parent == "-" or outcome == 0:  # outcome=0일 때 추가해야 시간초과 통과함
                break
            outcomes[parent].append(outcome)
            self = parent
            earn = outcome

    for k, v in outcomes.items():
        answer.append(sum(v))

    return answer


print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["sam", "emily", "jaimie", "edward"],
               [2, 3, 5, 4]))
