#constant

# #read user input
yard_greening_met = float(input())
price = yard_greening_met * 7.61
discount = price * 0.18

#logic
price_total = price - discount

#print output
print(f'Final price is: {price_total} lv.')
print(f'Discount is {discount} lv.')
