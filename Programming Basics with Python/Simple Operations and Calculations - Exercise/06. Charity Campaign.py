days = int(input())

chefs = int(input())

cakes = int(input())

waffles = int(input())

pancakes = int(input())

day_money = chefs * (cakes * 45 + waffles * 5.80 + pancakes * 3.20)

money = day_money * days * 7 / 8

print(f'{money:.2f}')
