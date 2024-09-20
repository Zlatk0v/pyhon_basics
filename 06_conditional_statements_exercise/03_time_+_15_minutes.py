# contant
MINUTES_IN_HOUR = 60
HOURS_IN_DAY = 24
EXTRA_MINUTES = 15

# input
hours = int(input())
minutes = int(input())

# logic
minutes += EXTRA_MINUTES

if minutes >= MINUTES_IN_HOUR:
    minutes -= MINUTES_IN_HOUR
    hours += 1

if hours >= HOURS_IN_DAY:
    hours -= HOURS_IN_DAY

# output
print(f'{hours}:{minutes:02d}')