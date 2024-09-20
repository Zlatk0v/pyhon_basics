# constant
BAD_GRADE = 4

# variables
sum_grades = 0
total_count_solved_task = 0
count_bad_grades = 0
last_task = ''
result = ''

# input
allowed_bad_grades = int(input())

# logic
while allowed_bad_grades > count_bad_grades:
    task_name = input()

# output
    if task_name == 'Enough':
        result = f'Average score: {sum_grades / total_count_solved_task:.2f}\n' \
                 f'Number of problems: {total_count_solved_task}\n' \
                 f'Last problem: {last_task}'
        break

    grade = int(input())

    if grade <= BAD_GRADE:
        count_bad_grades += 1

    sum_grades += grade
    total_count_solved_task += 1
    last_task = task_name
else:
    result = f'You need a break, {count_bad_grades} poor grades.'

print(result)
