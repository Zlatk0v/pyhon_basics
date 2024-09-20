# •	При скорост до 10 (включително) отпечатайте "slow"
# •	При скорост над 10 и до 50 (включително) отпечатайте "average"
# •	При скорост над 50 и до 150 (включително) отпечатайте "fast"
# •	При скорост над 150 и до 1000 (включително) отпечатайте "ultra fast"
# •	При по-висока скорост отпечатайте "extremely fast"

number = float(input())

if number <= 10:
    print("slow")
elif number <= 50:
    print("average")
elif number <= 150:
    print("fast")
elif number <= 1000:
    print("ultra fast")
else:
    print("extremely fast")