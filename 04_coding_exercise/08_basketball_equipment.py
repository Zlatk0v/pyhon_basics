#constant
PERCENT_SHOES = 0.40
PERCENT_TRAINING_TEAM = 0.20
PERCENT_BALL = 0.25
PERCENT_ACCESSORIES = 0.20

#read user input
annual_training_tax = int(input())

#logic
shoes = annual_training_tax - (annual_training_tax * PERCENT_SHOES)
training_team = shoes - (shoes * PERCENT_TRAINING_TEAM)
ball = training_team * PERCENT_BALL
accessories = ball * PERCENT_ACCESSORIES
total_sum = annual_training_tax + shoes + training_team + ball + accessories

#print output
print(total_sum)