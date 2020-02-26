number_of_floors = int(input())
units_on_floor = int(input())
for floor in range(number_of_floors, 0, -1):
    for unit in range(0, units_on_floor):
        if floor == number_of_floors:
            print(f'L{floor}{unit}', end=' ')
        elif floor % 2 == 0:
            print(f'O{floor}{unit}', end=' ')
        else:
            print(f'A{floor}{unit}', end=' ')
    print()
