budget = float(input())
stunts = int(input())
costume_cost = float(input())

decor = budget * 0.1

if stunts >= 150:
    costumes_total_cost = costume_cost * stunts * 0.9
else:
    costumes_total_cost = costume_cost * stunts

total_cost = decor + costumes_total_cost

if budget >= total_cost:
    print('Action!')
    print(f'Wingard starts filming with {budget - total_cost:.2f} leva left.')
else:
    print('Not enough money!')
    print(f'Wingard needs {total_cost - budget:.2f} leva more.')
