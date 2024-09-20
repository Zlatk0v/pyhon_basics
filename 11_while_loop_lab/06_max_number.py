# variables
import sys
max_num = -sys.maxsize

# input
command = input()

# logic
while command != 'Stop':
    current_num = int(command)
    if current_num > max_num:
        max_num = current_num

    command = input()

# output
print(max_num)
