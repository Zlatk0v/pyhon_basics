PERCENT_DISCOUNT = 0.15
PRICE_CARDS = 250
PERCENT_PROCESSOR = 0.35
PERCENT_RAM = 0.10

budget = float(input())
count_video = int(input())
count_processors = int(input())
count_ram = int(input())

sum_videos = count_video * PRICE_CARDS
sum_processor = count_processors * (sum_videos * PERCENT_PROCESSOR)
sum_ram = count_ram * (sum_videos * PERCENT_RAM)
sum_materials = sum_videos + sum_processor + sum_ram

if count_video > count_processors:
    sum_materials = sum_materials - (sum_materials * PERCENT_DISCOUNT)
    pass
if sum_materials > budget:
    print(f'Not enough money! You need {sum_materials - budget:.2f} leva more!')
else:
    print(f'You have {budget - sum_materials:.2f} leva left!')
