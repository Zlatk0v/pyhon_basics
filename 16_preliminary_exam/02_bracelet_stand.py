# input
pocket_money_per_day = float(input())
earnings_per_day = float(input())
total_expenses = float(input())
gift_price = float(input())

# constant
DAYS = 5

# variables
result = ''

# logic
total_pocket_money = pocket_money_per_day * DAYS
total_earnings = earnings_per_day * DAYS
total_saved_money = total_pocket_money + total_earnings - total_expenses

# output
if total_saved_money >= gift_price:
    result = f"Profit: {total_saved_money:.2f} BGN, the gift has been purchased."
else:
    insufficient_amount = gift_price - total_saved_money
    result = f"Insufficient money: {insufficient_amount:.2f} BGN."

print(result)
