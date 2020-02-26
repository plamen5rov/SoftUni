command = input()
prime_sum = 0
non_prime_sum = 0

while command != 'stop':
    number = int(command)
    if number < 0:
        print('Number is negative.')
        
    elif number == 0 or number % 2 == 0 and number != 2:
        non_prime_sum += number

    elif number % 3 == 0 and number != 3:
        non_prime_sum += number
    elif number % 5 == 0 and number != 5:
        non_prime_sum += number
    elif number % 7 == 0 and number != 7:
        non_prime_sum += number
    elif number % 10 == 0:
        non_prime_sum += number
    else:
        prime_sum += number

    command = input()

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}") 
