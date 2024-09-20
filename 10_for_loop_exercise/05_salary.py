# constant
FACEBOOK = 150
INSTAGRAM = 100
REDDIT = 50

# input
count_tabs = int(input())
salary = int(input())

result = ''

# logic
for _ in range(count_tabs):
    website = input()

    if website == 'Facebook':
        salary -= FACEBOOK

    elif website == 'Instagram':
        salary -= INSTAGRAM
    elif website == 'Reddit':
        salary -= REDDIT

    if salary <= 0:
        result = f'You have lost your salary.'
        break

else:
    result = salary


# output
print(result)
