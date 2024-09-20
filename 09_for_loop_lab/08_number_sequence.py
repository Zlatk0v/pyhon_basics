# input
n = int(input())

# logic
min_num = float('inf')
max_num = float('-inf')
result = ''
for _ in range(n):
    curr_num = int(input())
    if curr_num < min_num:
        min_num = curr_num

    if curr_num > max_num:
        max_num = curr_num
    result = f'Max number: {max_num}\nMin number: {min_num}'

# output
print(result)
