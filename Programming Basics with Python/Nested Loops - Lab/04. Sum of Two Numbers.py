x = int(input())
y = int(input())
sum = int(input())
counter = 0
combinations = 0
for x1 in range(x, y + 1):
    for x2 in range(x, y + 1):
        combinations += 1
        if x1 + x2 == sum:
            counter +=1
            print(f'Combination N:{combinations} ({x1} + {x2} = {sum})')
            break
    if counter > 0:
        break


if counter == 0:
    print(f'{combinations} combinations - neither equals {sum}')
