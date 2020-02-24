flowers_type = input()

number_of_flowers = int(input())

budget = int(input())

if flowers_type == 'Roses':
    if number_of_flowers <= 80:
        price = number_of_flowers * 5.00
    else:
        price = number_of_flowers * 5.00 * 0.90


elif flowers_type == 'Dahlias':
    if number_of_flowers <= 90:
        price = number_of_flowers * 3.80
    else:
        price = number_of_flowers * 3.80 * 0.85


elif flowers_type == 'Tulips':
    if number_of_flowers <= 80:
        price = number_of_flowers * 2.80
    else:
        price = number_of_flowers * 2.80 * 0.85

elif flowers_type == 'Narcissus':
    if number_of_flowers < 120:
        price = number_of_flowers * 3.00 * 1.15
    else:
        price = number_of_flowers * 3.00

elif flowers_type == 'Gladiolus':
    if number_of_flowers < 80:
        price = number_of_flowers * 2.50 * 1.20
    else:
        price = number_of_flowers * 2.50

if price <= budget:
    print(f"Hey, you have a great garden with {number_of_flowers} {flowers_type} and {budget - price:.2f} leva left.")
else:
    print(f"Not enough money, you need {price - budget:.2f} leva more.")
