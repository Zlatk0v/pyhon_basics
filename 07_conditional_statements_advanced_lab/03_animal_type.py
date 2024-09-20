# input
animal = input()

# variable
result = ''

# logic and output
if animal == 'dog':
    result = 'mammal'
elif animal == 'crocodile' or animal == 'tortoise' or animal == 'snake':
    result = 'reptile'
else:
    result = 'unknown'

print(result)
