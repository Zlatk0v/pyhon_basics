# input
n = int(input())
left_sum = 0
right_sum = 0

# left_sum
for _ in range(n):
    num = int(input())
    left_sum += num

# right_sum
for _ in range(n):
    num = int(input())
    right_sum += num

# output
if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    diff = abs(left_sum - right_sum)
    print(f"No, diff = {diff}")
