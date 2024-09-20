#constant
PRICE_NYLON = 1.50
PRICE_PAINT = 14.50
PRICE_THINNING = 5.00
PRICE_BAGS = 0.40
ADITIONALLY_PAINT = 0.10
ADITIONALLY_NYLON = 2
WORKER_PRICE_PER_HOUR = 0.30

#read user input
quantity_nylon = int(input())
quantity_paint = int(input())
quantity_thinning = int(input())
work_hours = int(input())

#logic
quantity_nylon += ADITIONALLY_NYLON
quantity_paint += (quantity_paint * ADITIONALLY_PAINT)
total_dum_materials = (quantity_nylon * PRICE_NYLON) \
                      + (quantity_paint * PRICE_PAINT) \
                      + (quantity_thinning * PRICE_THINNING) \
                      + PRICE_BAGS
total_sum_repairs = (total_dum_materials * WORKER_PRICE_PER_HOUR) * work_hours
total_sum = total_dum_materials + total_sum_repairs

#print output
print(total_sum)