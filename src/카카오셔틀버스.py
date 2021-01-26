from collections import deque

def solution(n, t, m, timetable):
    time_table = []
    for time in timetable:
        times = time.split(":")
        time_table.append(int(times[0]) * 60 + int(times[1]))
    time_table.sort()
    time_table = deque(time_table)

    candidate = 0
    for i in range(n):
        start_time = 9 * 60 + t * i
        time_list = []
        for _ in range(m):
            if time_table:
                time = time_table.popleft()
            else:
                break
            if time <= start_time:
                time_list.append(time)
            else:
                time_table.appendleft(time)
                break
        if len(time_list) < m:
            candidate = start_time
        else:
            candidate = max(time_list) - 1

    hour = str(candidate // 60)
    hour = hour if len(hour) == 2 else "0" + hour
    minute = str(candidate % 60)
    minute = minute if len(minute) == 2 else "0" + minute
    return hour + ":" + minute

print(solution(1,	1,	5	,["08:00", "08:01", "08:02", "08:03"]))
