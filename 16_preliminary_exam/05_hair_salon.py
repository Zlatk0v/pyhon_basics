# input
target = int(input())

# constant
HAIRCUT_MENS = 15
HAIRCUT_LADIES = 20
HAIRCUT_KIDS = 10
COLOR_TOUCH_UP = 20
COLOR_FULL_COLOR = 30

# variables
result = ''
total_money = 0

# logic

while True:
    command = input().strip()
    if command == "closed":
        break

    service_type = command

    if service_type == "haircut":
        haircut_type = input()
        if haircut_type == "mens":
            total_money += HAIRCUT_MENS
        elif haircut_type == "ladies":
            total_money += HAIRCUT_LADIES
        elif haircut_type == "kids":
            total_money += HAIRCUT_KIDS
    elif service_type == "color":
        color_type = input()
        if color_type == "touch up":
            total_money += COLOR_TOUCH_UP
        elif color_type == "full color":
            total_money += COLOR_FULL_COLOR

# output
    if total_money >= target:
        result = f"You have reached your target for the day!\n" \
                 f"Earned money: {total_money}lv."
        break

if total_money < target:
    needed_money = target - total_money
    result = f"Target not reached! You need {needed_money}lv. more.\n" \
             f"Earned money: {total_money}lv."

print(result)
