# input
student = input()

# variables
grades_sum = 0
current_class = 1
fails_count = 0

# logic
while current_class <= 12:
    grade = float(input())
    if grade < 4.00:
        fails_count += 1
        if fails_count >= 2:
            break
    else:
        grades_sum += grade
        current_class += 1

# output
if fails_count < 2:
    avg_grade = grades_sum / 12
    print(f'{student} graduated. Average grade: {avg_grade:.2f}')
else:
    print(f'{student} has been excluded at {current_class} grade')
