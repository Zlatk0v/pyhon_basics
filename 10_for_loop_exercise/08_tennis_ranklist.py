# constant
W = 2000
F = 1200
SF = 720

# input
count_tours = int(input())
points_for_season = int(input())

count_wins = 0
total_points = 0

# logic
for _ in range(count_tours):
    tournaments = input()

    if tournaments == 'W':
        count_wins += 1
        total_points += W
    elif tournaments == 'F':
        total_points += F
    elif tournaments == 'SF':
        total_points += SF

# output
print(f'Final points: {points_for_season + total_points}\n '
      f'Average points: {total_points // count_tours}\n '
      f'{count_wins / count_tours * 100:.2f}%')

