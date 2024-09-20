#constant
LITER_TO_ML = 1000

#read user input
length = int(input())
width = int(input())
height = int(input())
percent = float(input()) / 100

#logic
volume_fish_tank = length * width * height
volume_liters = volume_fish_tank / LITER_TO_ML
needed_liters = volume_liters * (1 - percent)

#print output
print(needed_liters)
