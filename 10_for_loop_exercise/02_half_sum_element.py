n = int(input())

max_num = float('-inf')
sum_number = 0

for num in range(n):
    number = int(input())

    if number > max_num:
        max_num = number

    sum_number += number

half_sum = sum_number - max_num

if max_num == half_sum:
    print(f'Yes')
    print(f'Sum = {max_num}')
else:
    print(f'No\n Diff = {abs(max_num - half_sum)}')