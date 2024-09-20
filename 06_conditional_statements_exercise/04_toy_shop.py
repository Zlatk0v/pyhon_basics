# constant
PUZZLE = 2.60
SPEAKING_TOY = 3
BEAR = 4.10
MINION = 8.20
TRUCK = 2
DISCOUNT_25 = 0.25
RENT = 0.10
NEEDED_TOYS_FOR_DISK = 50
# input
excursion = float(input())
number_of_puzzles = int(input())
number_of_speaking_toys = int(input())
number_of_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

total_number_of_toys = number_of_trucks \
                       + number_of_minions \
                       + number_of_bears \
                       + number_of_speaking_toys \
                       + number_of_puzzles

turnover = (PUZZLE * number_of_puzzles) \
           + (SPEAKING_TOY * number_of_speaking_toys) \
           + (BEAR * number_of_bears) \
           + (MINION * number_of_minions) \
           + (TRUCK * number_of_trucks)
# logic
if total_number_of_toys >= NEEDED_TOYS_FOR_DISK:
    turnover -= (turnover * DISCOUNT_25)

turnover -= (turnover * RENT)
# output
if turnover >= excursion:
    print(f'Yes! {turnover - excursion:.2f} lv left.')
else:
    print(f'Not enough money! {excursion - turnover:.2f} lv needed.')