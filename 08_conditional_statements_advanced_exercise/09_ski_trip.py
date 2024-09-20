# constant
PRICE_ROOM_FOR_ONE_PERSON = 18.00
PRICE_APARTMENT = 25.00
PRICE_PRESIDENT_APARTMENT = 35.00

# input
days = int(input())
room_type = input()
feedback = input()

# variables
nights = days - 1
total_price = 0.0

# logic
if room_type == "room for one person":
    total_price = nights * PRICE_ROOM_FOR_ONE_PERSON
elif room_type == "apartment":
    total_price = nights * PRICE_APARTMENT
elif room_type == "president apartment":
    total_price = nights * PRICE_PRESIDENT_APARTMENT

# discounts
if room_type == "apartment":
    if nights < 10:
        total_price *= 0.70
    elif 10 <= nights <= 15:
        total_price *= 0.65
    else:
        total_price *= 0.50
elif room_type == "president apartment":
    if nights < 10:
        total_price *= 0.90
    elif 10 <= nights <= 15:
        total_price *= 0.85
    else:
        total_price *= 0.80

# output
if feedback == "positive":
    total_price *= 1.25
else:
    total_price *= 0.90
print(f"{total_price:.2f}")
