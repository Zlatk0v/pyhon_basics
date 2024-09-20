#constant
DOG_FOOD = 2.50
CAT_FOOD = 4

# #read user input
dog_food_pack = float(input())
cat_food_pack = float(input())


#logic
result = (dog_food_pack * DOG_FOOD) \
         + (cat_food_pack * CAT_FOOD)
total_sum = f'{result} lv.'

#print output
print(total_sum)
