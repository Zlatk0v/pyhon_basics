day_from_the_week = input()

result = ''

if (day_from_the_week == 'Monday' \
        or day_from_the_week == 'Tuesday' \
        or day_from_the_week == 'Wednesday' \
        or day_from_the_week == 'Thursday' \
        or day_from_the_week == 'Friday'):
    result = 'Working day'
elif (day_from_the_week == 'Saturday' \
        or day_from_the_week == 'Sunday'):
    result = 'Weekend'
else:
    result = 'Error'

print(result)
