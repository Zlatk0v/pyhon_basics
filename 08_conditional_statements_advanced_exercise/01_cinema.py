# constant
PREMIERE = 12.00
NORMAL = 7.50
DISCOUNT = 5.00

# input
screening_type = input()
rows = int(input())
columns = int(input())

# logic
income = 0
cinema_capacity = rows * columns

if screening_type == 'Premiere':
    income = cinema_capacity * PREMIERE
elif screening_type == 'Normal':
    income = cinema_capacity * NORMAL
elif screening_type == 'Discount':
    income = cinema_capacity * DISCOUNT

# output
print(f'{income:.2f} leva')