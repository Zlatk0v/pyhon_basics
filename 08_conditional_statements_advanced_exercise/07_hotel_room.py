# constant
DISC_MAY_OCT_05 = 0.05
DISC_MAY_OCT_30 = 0.30
DISC_JUN_SEP_20 = 0.20
DISC_14_NIGHTS_10 = 0.10

# input
month = input()
count_nights = int(input())

# logic per prices
studio_price_per_night = 0.0
apartment_price_per_night = 0.0

if month == 'May' or month == 'October':
    studio_price_per_night = 50
    apartment_price_per_night = 65
elif month == 'June' or month == 'September':
    studio_price_per_night = 75.20
    apartment_price_per_night = 68.70
elif month == 'July' or month == 'August':
    studio_price_per_night = 76
    apartment_price_per_night = 77

# logic per studio total price
studio_total_price = studio_price_per_night * count_nights

if month == 'May' or month == 'October':
    if count_nights > 14:
        studio_total_price -= studio_total_price * DISC_MAY_OCT_30
    elif count_nights > 7:
        studio_total_price -= studio_total_price * DISC_MAY_OCT_05
elif month == 'June' or month == 'September':
    if count_nights > 14:
        studio_total_price -= studio_total_price * DISC_JUN_SEP_20

# logic per apartment total price
apartment_total_price = apartment_price_per_night * count_nights

if count_nights > 14:
    apartment_total_price -= apartment_total_price * DISC_14_NIGHTS_10

# output
apartment_result = f"Apartment: {apartment_total_price:.2f} lv."
studio_result = f"Studio: {studio_total_price:.2f} lv."
result = f"{apartment_result}\n{studio_result}"
print(result)
