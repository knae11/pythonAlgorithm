import heapq


def solution(table, languages, preference):
    process = []
    for item in table:
        row = item.split(" ")
        name = row[0]
        items = row[1:]
        items.reverse()
        candi = 0
        for i in range(len(languages)):
            if languages[i] in items:
                candi += (items.index(languages[i]) + 1) * preference[i]
        heapq.heappush(process, (-candi, name))

    return process[0][1]


print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#",
                "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
                "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",
                "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
                "GAME C++ C# JAVASCRIPT C JAVA"], ["PYTHON", "C++", "SQL"],
               [7, 5, 5]))
