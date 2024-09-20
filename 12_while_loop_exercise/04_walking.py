# constant
GOAL_STEP_DAY = 10_000

# variables
sum_steps = 0

# logic
while sum_steps < GOAL_STEP_DAY:
    steps = input()

    if steps == 'Going home':
        steps_to_home = int(input())
        sum_steps += steps_to_home
        break

    sum_steps += int(steps)

result = ''

# output
if sum_steps >= GOAL_STEP_DAY:
    result = f'Goal reached! Good job!\n' \
             f'{sum_steps - GOAL_STEP_DAY} steps over the goal!'
else:
    result = f'{GOAL_STEP_DAY - sum_steps} more steps to reach goal.'

print(result)
