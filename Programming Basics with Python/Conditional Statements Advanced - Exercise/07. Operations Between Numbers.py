first_number = int(input())

second_number = int(input())

command = input()

result = 0

if command == '+':

    result = first_number + second_number

    if result % 2 == 0:
        type = 'even'
    else:
        type = 'odd'

    print(f'{first_number} {command} {second_number} = {result} - {type}')

elif command == '-':

    result = first_number - second_number

    if result % 2 == 0:
        type = 'even'
    else:
        type = 'odd'

    print(f'{first_number} {command} {second_number} = {result} - {type}')

elif command == '*':

    result = first_number * second_number

    if result % 2 == 0:
        type = 'even'
    else:
        type = 'odd'

    print(f'{first_number} {command} {second_number} = {result} - {type}')

elif command == '/':

    if second_number != 0:

        result = first_number / second_number

        print(f'{first_number} {command} {second_number} = {result:.2f} ')
    else:
        print(f'Cannot divide {first_number} by zero')

elif command == '%':
    if second_number != 0:

        result = first_number % second_number

        print(f'{first_number} {command} {second_number} = {result} ')
    else:
        print(f'Cannot divide {first_number} by zero')
