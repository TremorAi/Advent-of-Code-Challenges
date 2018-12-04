import re
from collections import Counter
file_input = list(map(str.strip, open("day4/input.txt").readlines()))
# [1518-05-21 23:59] Guard #863 begins shift  year month day
re_log = re.compile(r"\[(\d+)-(\d+)-(\d+) (\d+):(\d+)\] (.+)")
guard_log = {}
log_sorted = []
guard_id = -1
guard_sleep = -1
guard_length = 0
max_guard_id = 0
HELP = 0
default_frequent = 0
winner_winner = 0
winner_winner_chicken_dinner = 0


def parse_line(line):
    year, month, day, hour, minuet, text = re_log.search(line).groups()
    guard_num = re.search(r'Guard #(\d+)', line)
    if guard_num:
        guard_num = int(guard_num[1])
    return int(year), int(month), int(day), int(hour), int(minuet), text, guard_num


for line in file_input:
    year, month, day, hour, minuet, text, guard_num = parse_line(line)
    log_sorted.append((year, month, day, hour, minuet, text, guard_num))

    if guard_num:
        if guard_num not in guard_log:
            guard_log[guard_num] = []
log_sorted.sort(key=lambda x: x[:5])
for thing in log_sorted:
    if thing[6]:
        guard_id = thing[6]
        print(f"{guard_id} is now on duty")
    if thing[5] == "falls asleep":
        print(f"{guard_id} has fallen asleepy pie")
        guard_sleep = int(thing[4])
    if thing[5] == "wakes up" or thing[6] and guard_sleep != -1:
        for i in range(guard_sleep, thing[4]):
            guard_log[guard_id].append(i)
        print(f"{guard_id} has awoken!")
        guard_sleep = -1
for r in guard_log:
    if guard_log[r]:
        THING = Counter(guard_log[r]).most_common(1)[0][0]
        print(THING)
    if len(guard_log[r]) > guard_length:
        guard_length = len(guard_log[r])
        max_guard_id = r
    # number = guard_log.count(THING)
    if guard_log[r].count(THING) > default_frequent:
        default_frequent = guard_log[r].count(THING)
        winner_winner = THING
        winner_winner_chicken_dinner = r

print(
    f"{max_guard_id} has a value {guard_length} minuet spent most {THING}")
print(f"HELP ME {max_guard_id * THING}")

print(f"{winner_winner * winner_winner_chicken_dinner}")
