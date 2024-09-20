#constant
SECONDS_IN_MINUTES = 60

#input
time_first = int(input())
time_second = int(input())
time_third = int(input())

#logic
sum_seconds = time_first + time_second + time_third #30+20+30 = 80
minutes = sum_seconds // SECONDS_IN_MINUTES
seconds = sum_seconds % SECONDS_IN_MINUTES


if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')


#OR

# print_text = f'{minutes}:0{seconds}' is seconds < 10 else f'{munites}:{seconds}'
#
# #OR
#
# print(f'{minutes}:{seconds:02d}') #3:7 = 07