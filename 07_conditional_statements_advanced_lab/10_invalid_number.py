# input

number = int(input())
result = ''

# logic

if 100 <= number <= 200 or number == 0:
    result = ''
elif number < 0 or 100 > number or number > 200:
    result = 'invalid'

# output

print(result)
