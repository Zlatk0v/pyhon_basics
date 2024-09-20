#constant
PRICE_PACKAGE_PENS = 5.80
PRICE_PACKAGE_MARKERS = 7.20
PRICE_LITER_DETERGENT = 1.20

#read user input
count_packages_pens = int(input())
count_packages_markers = int(input())
liter_detergent = int(input())
percent_discount = int(input()) / 100

#logic
total_sum_materials_without_disc = (count_packages_pens * PRICE_PACKAGE_PENS) \
                                   + (count_packages_markers * PRICE_PACKAGE_MARKERS) \
                                   + (liter_detergent * PRICE_LITER_DETERGENT)

total_sum_materials_with_disc = total_sum_materials_without_disc - (total_sum_materials_without_disc * percent_discount)

#print output
print(total_sum_materials_with_disc)