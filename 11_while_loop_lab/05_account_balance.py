# input
command = input()

# logic and print
total_sum = 0

while command != 'NoMoreMoney':
    current_num = float(command)
    if current_num < 0:
        print('Invalid operation!')
        break
    print(f'Increase: {current_num:.2f}')
    total_sum += float(command)
    command = input()
print(f'Total: {total_sum:.2f}')
