# constant
GROUP_1 = 5
GROUP_2 = 12
GROUP_3 = 25
GROUP_4 = 40

# input
count_group = int(input())

count_group_1 = 0
count_group_2 = 0
count_group_3 = 0
count_group_4 = 0
count_group_5 = 0


# logic
for _ in range(count_group):
    group = int(input())

    if group <= GROUP_1:
        count_group_1 += group

    elif group <= GROUP_2:
        count_group_2 += group
    elif group <= GROUP_3:
        count_group_3 += group
    elif group <= GROUP_4:
        count_group_4 += group
    else:
        count_group_5 += group

total_people = count_group_1 + count_group_2 + count_group_3 + count_group_4 + count_group_5

# output
print(f'{count_group_1 / total_people * 100: .2f}%\n '
      f'{count_group_2 / total_people * 100: .2f}%\n '
      f'{count_group_3 / total_people * 100: .2f}%\n '
      f'{count_group_4 / total_people * 100: .2f}%\n '
      f'{count_group_5 / total_people * 100: .2f}%\n ')
