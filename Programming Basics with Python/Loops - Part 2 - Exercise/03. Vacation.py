needed_money = float(input())
money = float(input())

days = 0
spending_days = 0

while money < needed_money and spending_days < 5:
    action = input()
    amount = float(input())
    days += 1

    if action == "save":
        money += amount
        spending_days = 0
    elif action == "spend":
        money -= amount
        spending_days += 1
        if money < 0:
            money = 0

if spending_days == 5:
    print("You can\'t save the money.")
    print(days)
if money >= needed_money:
    print(f'You saved the money for {days} days.')
