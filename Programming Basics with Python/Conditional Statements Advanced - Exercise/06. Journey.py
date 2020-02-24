budget = float(input())

season = input()

if budget <=100:
    destination = "Bulgaria"
    if season == 'summer':
        place = 'Camp'
        money_spent = budget * 0.30
    elif season == 'winter':
        place = 'Hotel'
        money_spent = budget * 0.70

elif budget <=1000:
    destination = "Balkans"
    if season == 'summer':
        place = 'Camp'
        money_spent = budget * 0.40
    elif season == 'winter':
        place = 'Hotel'
        money_spent = budget * 0.80

else:
    destination = "Europe"
    
    place = 'Hotel'
    money_spent = budget * 0.90

print(f'Somewhere in {destination}')

print(f'{place} - {money_spent:.2f}')
