import math
side_a = int(input())
side_b = int(input())

cake_pieces = side_a * side_b
initial_cake = cake_pieces


command = input()

while command != 'STOP':
    taken_pieces = int(command)
    cake_pieces = cake_pieces - taken_pieces
    if cake_pieces < 0:
        break
    else:
        command = input()

if cake_pieces > 0:
    print(f'{cake_pieces} pieces are left.')
else:
    print(f'No more cake left! You need {abs(cake_pieces)} pieces more.')
