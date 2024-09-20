# constant
P1 = 200
P2 = 400
P3 = 600
P4 = 800

# input

n = int(input())

count_p1 = 0
count_p2 = 0
count_p3 = 0
count_p4 = 0
count_p5 = 0


# logic

for _ in range(n):
    number = int(input())

    if number < P1:
        count_p1 += 1

    elif number < P2:
        count_p2 += 1

    elif number < P3:
        count_p3 += 1

    elif number < P4:
        count_p4 += 1

    else:
        count_p5 += 1

total_count_p = count_p1 + count_p2 + count_p3 + count_p4 + count_p5


# output

print(f'{count_p1 / total_count_p * 100:.2f}%')
print(f'{count_p2 / total_count_p * 100:.2f}%')
print(f'{count_p3 / total_count_p * 100:.2f}%')
print(f'{count_p4 / total_count_p * 100:.2f}%')
print(f'{count_p5 / total_count_p * 100:.2f}%')
