#read user input
deposit_amount = float(input())
deposit_term = int(input())
annual_percent = float(input()) / 100

#logic
total_amount = deposit_amount + deposit_term * ((deposit_amount * annual_percent) / 12)

#print output
print(total_amount)