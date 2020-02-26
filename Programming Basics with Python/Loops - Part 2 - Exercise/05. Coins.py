import math

change = math.floor(float(input()) * 100)

counter = 0

coins = 0

while change != 0:

    if change // 200 > 0:
        coins = change // 200
        counter += coins
        change = math.ceil(change - coins * 200)
    elif change // 100 > 0:
        coins = change // 100
        counter += coins
        change = math.ceil(change - coins * 100)
    elif change // 50 > 0:
        coins = change // 50
        counter += coins
        change = math.ceil(change - coins * 50)
    elif change // 20 > 0:
        coins = change // 20
        counter += coins
        change = math.ceil(change - coins * 20)
    elif change // 10 > 0:
        coins = change // 10
        counter += coins
        change = math.ceil(change - coins * 10)
    elif change // 5 > 0:
        coins = change // 5
        counter += coins
        change = math.ceil(change - coins * 5)
    elif change // 2 > 0:
        coins = change // 2
        counter += coins
        change = math.ceil(change - coins * 2)
    else:
        counter += 1
        change = 0

print(f'{counter:.0f}')
