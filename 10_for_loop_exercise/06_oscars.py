# constant
RESULT = 1250.5

# input
actor_name = input()
academy_points = float(input())
count_assessors = int(input())

result = ''

# logic
for _ in range(count_assessors):
    judge_name = input()
    judge_points = float(input())

    academy_points += len(judge_name) * judge_points / 2

    if academy_points > RESULT:
        result = f'Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!'
        break
    else:
        result = f'Sorry, {actor_name} you need {RESULT - academy_points:.1f} more!'

# output
print(result)
