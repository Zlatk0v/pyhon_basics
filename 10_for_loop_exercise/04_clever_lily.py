# constant
BROTHER_MONEY = 1
INCREASE_MONEY_BIRTHDAY = 10

# input

age = int(input())
price_washing = float(input())
price_toy = int(input())

birth_money = 10
count_toys = 0
total_money = 0


# logic

for year in range(1, age + 1):

    if year % 2 == 0:
        total_money += (birth_money - BROTHER_MONEY)
        birth_money += INCREASE_MONEY_BIRTHDAY

    else:
        count_toys += 1

total_money += (count_toys * price_toy)

result = ''

if total_money >= price_washing:
    result = f'Yes! {total_money - price_washing:.2f}'
else:
    result = f'No! {price_washing- total_money:.2f}'

# output
print(result)
