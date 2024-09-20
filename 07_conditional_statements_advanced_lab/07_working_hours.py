# input

hour_from_the_day = int(input())
day_from_the_week = input()
result = ''

# logic

if 10 <= hour_from_the_day <= 18:
    if day_from_the_week == 'Monday':
        result = 'open'
    elif day_from_the_week == 'Tuesday':
        result = 'open'
    elif day_from_the_week == 'Wednesday':
        result = 'open'
    elif day_from_the_week == 'Thursday':
        result = 'open'
    elif day_from_the_week == 'Friday':
        result = 'open'
    elif day_from_the_week == 'Saturday':
        result = 'open'
    elif day_from_the_week == 'Sunday':
        result = 'closed'
else:
    result = 'closed'

# output

print(result)
