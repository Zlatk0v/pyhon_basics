# input
number_of_students = int(input())

# variables
count_fail = 0
count_3_99 = 0
count_4_99 = 0
count_top_students = 0
total_grades_sum = 0

# logic
for _ in range(number_of_students):
    grade = float(input())
    total_grades_sum += grade
    if grade < 3.00:
        count_fail += 1
    elif 3.00 <= grade <= 3.99:
        count_3_99 += 1
    elif 4.00 <= grade <= 4.99:
        count_4_99 += 1
    elif grade >= 5.00:
        count_top_students += 1

percent_fail = (count_fail / number_of_students) * 100
percent_3_99 = (count_3_99 / number_of_students) * 100
percent_4_99 = (count_4_99 / number_of_students) * 100
percent_top_students = (count_top_students / number_of_students) * 100

average_grade = total_grades_sum / number_of_students

# output
print(f"Top students: {percent_top_students:.2f}%\n"
      f"Between 4.00 and 4.99: {percent_4_99:.2f}%\n"
      f"Between 3.00 and 3.99: {percent_3_99:.2f}%\n"
      f"Fail: {percent_fail:.2f}%\n"
      f"Average: {average_grade:.2f}")
