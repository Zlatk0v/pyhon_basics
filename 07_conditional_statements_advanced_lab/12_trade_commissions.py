# input
city = input()
sales = float(input())

# logic
result = 'error'
commission_amount = 0.0

if city == 'Sofia':
    if 0 <= sales <= 500:
        commission_amount = sales * 0.05
    elif 500 < sales <= 1000:
        commission_amount = sales * 0.07
    elif 1000 < sales <= 10000:
        commission_amount = sales * 0.08
    elif sales > 10000:
        commission_amount = sales * 0.12
elif city == 'Varna':
    if 0 <= sales <= 500:
        commission_amount = sales * 0.045
    elif 500 < sales <= 1000:
        commission_amount = sales * 0.075
    elif 1000 < sales <= 10000:
        commission_amount = sales * 0.1
    elif sales > 10000:
        commission_amount = sales * 0.13
elif city == 'Plovdiv':
    if 0 <= sales <= 500:
        commission_amount = sales * 0.055
    elif 500 < sales <= 1000:
        commission_amount = sales * 0.08
    elif 1000 < sales <= 10000:
        commission_amount = sales * 0.12
    elif sales > 10000:
        commission_amount = sales * 0.145

if commission_amount > 0:
    result = f"{commission_amount:.2f}"

# output
print(result)
