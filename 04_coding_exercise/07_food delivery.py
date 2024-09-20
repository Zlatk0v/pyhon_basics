#constant
PRICE_CHICKEN_MENU = 10.35
PRICE_FISH_MENU = 12.40
PRICE_VEGATARIAN_MENU = 8.15
DELIVERY_PRICE = 2.50
DESSERT_PERCENT = 0.20

#read user input
count_chicken_menus = int(input())
count_fish_menus = int(input())
count_vеg_menus = int(input())

#logic
total_sum_menus = (count_chicken_menus * PRICE_CHICKEN_MENU) \
                  + (count_fish_menus * PRICE_FISH_MENU) \
                  + (count_vеg_menus * PRICE_VEGATARIAN_MENU)
total_sum = total_sum_menus + (total_sum_menus * DESSERT_PERCENT) + DELIVERY_PRICE

#print output2
print(total_sum)
