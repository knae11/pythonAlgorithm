# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# pass

user_input = int(input())
start_times = []
end_times = []


def time_to_int(time):
    hh, mm = time.split(":")
    return int(hh) * 60 + int(mm)


for _ in range(user_input):
    start, delimiter, end = input().split()
    start_times.append(time_to_int(start))
    end_times.append(time_to_int(end))


def int_to_time(number):
    hh = number // 60
    mm = number % 60
    return str(hh).zfill(2) + ":" + str(mm).zfill(2)


def solution(start_times, end_times):
    start = max(start_times)
    end = min(end_times)
    if start > end:
        return -1
    return int_to_time(start) + " ~ " + int_to_time(end)


print(solution(start_times, end_times))
