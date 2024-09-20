# input
target_number = int(input())

# variables
combinations = 0

# logic
for x1 in range(target_number + 1):
    for x2 in range(target_number + 1):
        for x3 in range(target_number + 1):
            if x1 + x2 + x3 == target_number:
                combinations += 1

# output
print(combinations)
