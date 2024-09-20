# constant
WRAPPING_PAPER = 5.80
LEATHER = 7.20
GLUE = 1.20

# input
number_of_rolls_of_wrapping_paper = int(input())
number_of_leather_rolls = int(input())
liters_glue = float(input())
percent_discount = int(input())

# logic
total_cost_paper = number_of_rolls_of_wrapping_paper * WRAPPING_PAPER
total_cost_leather = number_of_leather_rolls * LEATHER
total_cost_glue = liters_glue * GLUE

total_cost = total_cost_paper + total_cost_leather + total_cost_glue

discount = (percent_discount / 100) * total_cost
final_cost = total_cost - discount

# output
print(f"{final_cost:.3f}")
