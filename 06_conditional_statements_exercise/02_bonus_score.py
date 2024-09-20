#constant
THRESHOLD_HUNDRED = 100
THRESHOLD_THOUSAND = 1000
FIVE_BONUS_POINTS = 5
TWENTY_PERCENT_PRICE = 0.20
TEN_PERCENT_PRICE = 0.10
EVEN_NUMBER_BONUS_POINT = 1
ENDS_FIVE_BONUS_POINT = 2

#input
number = int(input())
bonus_points = 0

#LOGIC

if number <= THRESHOLD_HUNDRED:
    bonus_points += FIVE_BONUS_POINTS
elif number > 1000:
    bonus_points += (number * TEN_PERCENT_PRICE)
else:
    bonus_points += (number * TWENTY_PERCENT_PRICE)

if number % 2 == 0:
    bonus_points += EVEN_NUMBER_BONUS_POINT
elif number % 10 == 5:
    bonus_points += ENDS_FIVE_BONUS_POINT

print(bonus_points)
print(bonus_points + number)