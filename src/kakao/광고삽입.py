def solution(play_time, adv_time, logs):
    total_play = convert_sec(play_time)
    total_adv = convert_sec(adv_time)
    all_times = [0 for _ in range(total_play + 1)]
    for log in logs:
        split = log.split("-")
        start, end = split[0], split[1]
        start_time, end_time = convert_sec(start), convert_sec(end)
        all_times[start_time] += 1
        all_times[end_time] -= 1
    for i in range(1, len(all_times)):
        all_times[i] = all_times[i] + all_times[i - 1]
    # 누적
    for i in range(1, len(all_times)):
        all_times[i] = all_times[i] + all_times[i - 1]
    view = 0
    max_time = 0
    for i in range(total_adv - 1, total_play):
        if i >= total_adv:
            if view < all_times[i] - all_times[i - total_adv]:
                view = all_times[i] - all_times[i - total_adv]
                max_time = i - total_adv + 1
        else:
            if view < all_times[i]:
                view = all_times[i]
                max_time = i - total_adv + 1

    return convert_time(max_time)


def convert_time(sec):
    time = []
    times = [3600, 60, 1]
    for i in range(3):
        result = str(sec // times[i]).zfill(2)
        time.append(result)
        sec = sec % times[i]
    return ":".join(time)


def convert_sec(play_time):
    total_play = 0
    times = [3600, 60, 1]
    play_times = play_time.split(":")
    for i in range(3):
        total_play += int(play_times[i]) * times[i]
    return total_play


print(solution("02:03:55", "00:14:15",
               ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29",
                "01:30:59-01:53:29", "01:37:44-02:02:30"]))
