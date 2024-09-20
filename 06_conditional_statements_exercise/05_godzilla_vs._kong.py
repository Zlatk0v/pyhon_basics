# constant
DECOR = 0.10
DRESS_DISCOUNT = 0.10
NEEDED_FOR_DISC = 151

# input
budget = float(input())
number_of_statics = int(input())
price_dress_per_static = float(input())

# logic
price_decor = budget * DECOR
clothing_sum = number_of_statics * price_dress_per_static

if number_of_statics >= NEEDED_FOR_DISC:
    clothing_sum -= (clothing_sum * DRESS_DISCOUNT)

needed_money = price_decor + clothing_sum


# output
if needed_money > budget:
    print(f'Not enough money!')
    print(f'Wingard needs {needed_money - budget:.2f} leva more.')
else:
    print(f'Action!')
    print(f'Wingard starts filming with {budget - needed_money:.2f} leva left.')