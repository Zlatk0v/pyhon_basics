# input
ROSE = 5.00
DAHLIAS = 3.80
TULIPS = 2.80
NARCISSUS = 3.00
GLADIOLUS = 2.50

THRESHOLD_80 = 80
THRESHOLD_90 = 90
THRESHOLD_120 = 120

PERCENT_DISCOUNT_10 = 0.10
PERCENT_DISCOUNT_15 = 0.15
PERCENT_INCREASE_15 = 0.15
PERCENT_INCREASE_20 = 0.20

type_flours = input()
count_flours = int(input())
budget = int(input())

price_flours = 0

if type_flours == 'Roses':
    price_flours += (count_flours * ROSE)
    if count_flours > THRESHOLD_80:
        price_flours -= (price_flours * PERCENT_DISCOUNT_10)

elif type_flours == 'Dahlias':
    price_flours += (count_flours * DAHLIAS)
    if count_flours > THRESHOLD_90:
        price_flours -= (price_flours * PERCENT_DISCOUNT_15)

elif type_flours == 'Tulips':
    price_flours += (count_flours * TULIPS)
    if count_flours > THRESHOLD_80:
        price_flours -= (price_flours * PERCENT_DISCOUNT_15)

elif type_flours == 'Narcissus':
    price_flours += (count_flours * NARCISSUS)
    if count_flours < THRESHOLD_120:
        price_flours += (price_flours * PERCENT_INCREASE_15)

elif type_flours == 'Gladiolus':
    price_flours += (count_flours * GLADIOLUS)
    if count_flours < THRESHOLD_80:
        price_flours += (price_flours * PERCENT_INCREASE_20)

if budget >= price_flours:
    print(f"Hey, you have a great garden with {count_flours} {type_flours} and {budget - price_flours:.2f} leva left.")
else:
    print(f"Not enough money, you need {price_flours - budget:.2f} leva more.")
