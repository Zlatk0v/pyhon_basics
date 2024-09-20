# input
fruit = input()
day_from_the_week = input()
quantity = float(input())

# variables
result = ''
price = 0.0

# logic
if day_from_the_week == 'Monday' \
        or day_from_the_week == 'Tuesday' \
        or day_from_the_week == 'Wednesday' \
        or day_from_the_week == 'Thursday' \
        or day_from_the_week == 'Friday':
    if fruit == 'banana':
        price = 2.50
    elif fruit == 'apple':
        price = 1.20
    elif fruit == 'orange':
        price = 0.85
    elif fruit == 'grapefruit':
        price = 1.45
    elif fruit == 'kiwi':
        price = 2.70
    elif fruit == 'pineapple':
        price = 5.50
    elif fruit == 'grapes':
        price = 3.85
    else:
        result = 'error'
elif day_from_the_week == 'Saturday' \
        or day_from_the_week == 'Sunday':
    if fruit == 'banana':
        price = 2.70
    elif fruit == 'apple':
        price = 1.25
    elif fruit == 'orange':
        price = 0.90
    elif fruit == 'grapefruit':
        price = 1.60
    elif fruit == 'kiwi':
        price = 3.00
    elif fruit == 'pineapple':
        price = 5.60
    elif fruit == 'grapes':
        price = 4.20
    else:
        result = 'error'
else:
    result = 'error'

# output
if result != 'error':
    total_price = quantity * price
    result = f"{quantity * price:.2f}"

print(result)
