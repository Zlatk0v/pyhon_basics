# input
command = input()

# logic and output
while command != 'End':
    destination = command
    budget_needed = float(input())

    money = 0
    while money < budget_needed:
        current_saving = float(input())
        money += current_saving

    print(f'Going to {destination}!')

    command = input()
