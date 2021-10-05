from collections import defaultdict


def solution(tickets):
    answer = []
    connections = defaultdict(list)

    for ticket in tickets:
        connections[ticket[0]].append(ticket[1])
    for k in connections.keys():
        connections[k].sort(reverse=True)
    # 중간 안전지대를 두자!!
    stack = ["ICN"]
    while stack:
        curr = stack[-1]
        if not connections[curr]:
            answer.append(stack.pop())
        else:
            stack.append(connections[curr].pop())
    answer.reverse()
    return answer


print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"],
                ["ATL", "SFO"]]))
