# input

day_from_the_week = input()
result = ''

# logic

if day_from_the_week == 'Monday':
    result = '12'
elif day_from_the_week == 'Tuesday':
    result = '12'
elif day_from_the_week == 'Wednesday':
    result = '14'
elif day_from_the_week == 'Thursday':
    result = '14'
elif day_from_the_week == 'Friday':
    result = '12'
elif day_from_the_week == 'Saturday':
    result = '16'
elif day_from_the_week == 'Sunday':
    result = '16'
else:
    result = 'closed'

# output

print(result)
