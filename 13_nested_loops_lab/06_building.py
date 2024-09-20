# input
floors = int(input())
rooms = int(input())

# logic
for f in range(floors, 0, -1):
    for r in range(rooms):
        if f == floors:
            lead = 'L'
        elif f % 2 == 0:
            lead = 'O'
        else:
            lead = 'A'

        print(f'{lead}{f}{r}', end=' ')

    print()
