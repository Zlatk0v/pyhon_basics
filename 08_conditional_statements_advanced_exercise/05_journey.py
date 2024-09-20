# input
budget = float(input())
season = input()

# variables
destination = ''
result = ''
type_place = ''

# logic and output
if 0 < budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        budget = (budget * 0.30)
        type_place = 'Camp'
        result = f'Somewhere in {destination}\n{type_place} - {budget:.2f}'
    elif season == 'winter':
        budget = (budget * 0.70)
        type_place = 'Hotel'
        result = f'Somewhere in {destination}\n{type_place} - {budget:.2f}'
    print(result)

if 100 <= budget <= 1_000:
    destination = 'Balkans'
    if season == 'summer':
        budget = (budget * 0.40)
        type_place = 'Camp'
        result = f'Somewhere in {destination}\n{type_place} - {budget:.2f}'
    elif season == 'winter':
        budget = (budget * 0.80)
        type_place = 'Hotel'
        result = f'Somewhere in {destination}\n{type_place} - {budget:.2f}'
    print(result)

if budget >= 1_000:
    destination = 'Europe'
    budget = (budget * 0.90)
    type_place = 'Hotel'
    result = f'Somewhere in {destination}\n{type_place} - {budget:.2f}'
    print(result)
