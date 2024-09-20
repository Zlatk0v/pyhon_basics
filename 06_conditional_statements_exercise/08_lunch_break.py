from math import ceil

serial_name = input()
epizode_duration = int(input())
break_duration = int(input())

time_lunch = break_duration / 8
time_chill = break_duration / 4

total_time = epizode_duration + time_lunch + time_chill
time_left = break_duration - total_time


if time_left >= 0:
    print(f'You have enough time to watch {serial_name} and left with {ceil(time_left)} minutes free time.')
else:
    print(f"You don't have enough time to watch {serial_name}, you need {ceil(abs(time_left))} more minutes.")