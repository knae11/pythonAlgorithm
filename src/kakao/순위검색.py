LANG = 0
POSI = 1
EXPE = 2
FOOD = 3
SCOR = 4


def solution(info, query):
    answer = []
    division = {"frontend":
                    {"senior":
                         {"pizza": [],
                          "chicken": []
                          },
                     "junior":
                         {"pizza": [],
                          "chicken": []
                          }
                     },
                "backend":
                    {"senior":
                         {"pizza": [],
                          "chicken": []
                          },
                     "junior":
                         {"pizza": [],
                          "chicken": []
                          }
                     }
                }
    applicants = {"python": division,
                  "cpp": division,
                  "java": division}

    for person in info:
        person_info = person.split(" ")
        applicants[person_info[LANG]][person_info[POSI]][person_info[EXPE]][
            person_info[FOOD]].append(int(person_info[SCOR]))
    print(applicants)
    for que in query:
        que_info = que.replace(" and ", " ").split(" ")
        result = 0
        # TODO : '-'인 경우 불가
        for score in applicants[que_info[LANG]][que_info[POSI]][que_info[EXPE]] \
                [que_info[FOOD]]:
            if score >= int(que_info[SCOR]):
                result += 1
        print(result)
        answer.append(result)
    return answer


print(solution(
    ["java backend junior pizza 150", "python frontend senior chicken 210",
     "python frontend senior chicken 150", "cpp backend senior pizza 260",
     "java backend junior chicken 80", "python backend senior chicken 50"],
    ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
     "cpp and - and senior and pizza 250", "- and backend and senior and - 150",
     "- and - and - and chicken 100", "- and - and - and - 150"]
))
