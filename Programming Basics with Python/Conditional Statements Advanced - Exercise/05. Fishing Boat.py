budget = int(input())

season = input()

fishermen = int(input())

if season == 'Spring':
    boat_rent = 3000
elif season == 'Winter':
    boat_rent = 2600
else:
    boat_rent = 4200

if fishermen <= 6:
    boat_rent = boat_rent * 0.90
elif 7 <= fishermen <= 11:
    boat_rent = boat_rent * 0.85
else:
    boat_rent = boat_rent * 0.75

if (season != 'Autumn') and (fishermen % 2 == 0):
    boat_rent = boat_rent * 0.95

if boat_rent <= budget:
    print(f"Yes! You have {budget - boat_rent:.2f} leva left.")
else:
    print(f"Not enough money! You need {boat_rent - budget:.2f} leva.")
