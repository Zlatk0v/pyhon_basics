# constant
PRICE_RENT_SPRING = 3000
PRICE_RENT_SUMMER_AUTUMN = 4200
PRICE_RENT_WINTER = 2600

THRESHOLD_GROUP_6 = 6
THRESHOLD_GROUP_7 = 7
THRESHOLD_GROUP_11 = 11
THRESHOLD_GROUP_12 = 12

DISC_10 = 0.10
DISC_15 = 0.15
DISC_25 = 0.25
DISC_05 = 0.05

# input
budget = int(input())
season = input()
count_fishers = int(input())

# logic
price_rent = 0

if season == 'Spring':
    price_rent = PRICE_RENT_SPRING
    if count_fishers <= THRESHOLD_GROUP_6:
        price_rent -= (price_rent * DISC_10)
    elif THRESHOLD_GROUP_7 < count_fishers <= THRESHOLD_GROUP_11:
        price_rent -= (price_rent * DISC_15)
    elif count_fishers > THRESHOLD_GROUP_12:
        price_rent -= (price_rent * DISC_25)

elif season == 'Summer' or season == 'Autumn':
    price_rent = PRICE_RENT_SUMMER_AUTUMN
    if count_fishers <= THRESHOLD_GROUP_6:
        price_rent -= (price_rent * DISC_10)
    elif THRESHOLD_GROUP_7 < count_fishers <= THRESHOLD_GROUP_11:
        price_rent -= (price_rent * DISC_15)
    elif count_fishers > THRESHOLD_GROUP_12:
        price_rent -= (price_rent * DISC_25)

else:
    price_rent = PRICE_RENT_WINTER
    if count_fishers <= THRESHOLD_GROUP_6:
        price_rent -= (price_rent * DISC_10)
    elif THRESHOLD_GROUP_7 < count_fishers <= THRESHOLD_GROUP_11:
        price_rent -= (price_rent * DISC_15)
    elif count_fishers > THRESHOLD_GROUP_12:
        price_rent -= (price_rent * DISC_25)

if season != 'Autumn' and count_fishers % 2 == 0:
    price_rent -= (price_rent * DISC_05)

# print
if budget >= price_rent:
    print(f'Yes! You have {budget - price_rent:.2f} leva left.')
else:
    print(f'Not enough money! You need {price_rent - budget:.2f} leva.')

