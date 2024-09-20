# input
number_of_people = int(input())
season = input()

# variables
price_per_person = 0

# logic
if number_of_people <= 5:
    if season == 'spring':
        price_per_person = 50.00

    elif season == 'summer':
        price_per_person = 48.50

    elif season == 'autumn':
        price_per_person = 60.00

    elif season == 'winter':
        price_per_person = 86.00


if number_of_people > 5:
    if season == 'spring':
        price_per_person = 48.00

    elif season == 'summer':
        price_per_person = 45.00

    elif season == 'autumn':
        price_per_person = 49.50

    elif season == 'winter':
        price_per_person = 85.00

total_price = price_per_person * number_of_people

if season == "summer":
    total_price *= 0.85
elif season == "winter":
    total_price *= 1.08

# output
print(f"{total_price:.2f} leva.")
