month = input()

nights = int(input())

studio = 0
apartment = 0

if month == 'May' or month == 'October':

    apartment = 65 * nights
    if 7 < nights <= 14:
        studio = 50 * 0.95 * nights
    elif nights > 14:
        studio = 50 * 0.70 * nights
        apartment = 65 * 0.90 * nights
    else:
        studio = 50 * nights
        apartment = 65 * nights

elif month == 'June' or month == 'September':

    apartment = 68.70 * nights

    if nights > 14:
        studio = 75.20 * 0.80 * nights
        apartment = 68.70 * 0.90 * nights
    else:
        studio = 75.20 * nights

elif month == 'July' or month == 'August':
    studio = 76 * nights

    if nights > 14:
        apartment = 77 * 0.90 * nights
    else:
        apartment = 77 * nights

print(f'Apartment: {apartment:.2f} lv.')

print(f'Studio: {studio:.2f} lv.')
