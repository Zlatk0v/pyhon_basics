student_tickets, standard_tickets, kid_tickets = 0, 0, 0
result = ''

while True:
    movie_name = input()

    if movie_name == 'Finish':
        break

    capacity = int(input())
    sold_tickets = 0

    while capacity > sold_tickets:
        tickets_type = input()

        if tickets_type == 'End':
            break

        if tickets_type == 'student':
            student_tickets += 1

        elif tickets_type == 'standard':
            standard_tickets += 1

        elif tickets_type == 'kid':
            kid_tickets += 1

        sold_tickets += 1

    result += f'{movie_name} - {sold_tickets / capacity * 100:.2f}% full.\n'

total_tickets = student_tickets + standard_tickets + kid_tickets

result += f'Total tickets: {total_tickets}\n' \
          f'{student_tickets / total_tickets * 100:.2f}% student tickets.\n' \
          f'{standard_tickets / total_tickets * 100:.2f}% standard tickets.\n ' \
          f'{kid_tickets / total_tickets * 100:.2f}% kids tickets.'

print(result)
