
def ten_percent(input):
    return input // 10

def solution(enroll, referral, seller, amount):
    answer = []
    root = Node("-")
    for i in range(len(enroll)):
        parent = referral[i]
        child = Node(enroll[i])
        root.find(parent).add_child(child)

    #todo
    for i in range(len(seller)):
        root.set_money(seller[i],amount[i]*100)

    for i in range(len(seller)):
        print(root.find(seller[i]).money)
    return answer

class Node:
    def __init__(self, data):
        self.data = data
        self.money = 0
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

    def find(self, x):
        if self.data is x: return self
        for node in self.children:
            n = node.find(x)
            if n: return n
        return None

    # todo
    def set_money(self, x, money):
        if self.data is x:
            self.money+= money - ten_percent(money)
            return self
        for node in self.children:
            n = node.set_money(x, money)
            if n:
                node.money += ten_percent(money)
                return n
        return None





print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["young", "john", "tod", "emily", "mary"],
               [12, 4, 2, 5, 10]))
