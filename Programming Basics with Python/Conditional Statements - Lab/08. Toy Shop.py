price_of_trip = float(input())

puzzles = int(input())

dolls = int(input())

bears = int(input())

minions = int(input())

trucks = int(input())

toys = puzzles + dolls + bears + minions + trucks

puzzles_profit = puzzles * 2.60

dolls_profit = dolls * 3

bears_profit = bears * 4.10

minions_profit = minions * 8.20

trucks_profit = trucks * 2

profit = puzzles_profit + dolls_profit + bears_profit + minions_profit + trucks_profit

if toys >= 50:
    profit = profit * 0.75
else:
    profit = profit

money = profit * 0.9

result = 0

if money >= price_of_trip:
    result = money - price_of_trip
    print(f'Yes! {result:.2f} lv left.')
else:
    result = price_of_trip - money
    print(f'Not enough money! {result:.2f} lv needed.')
