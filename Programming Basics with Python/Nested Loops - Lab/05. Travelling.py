saved_money = 0

while True:
    destination = input()
    if destination == "End":
        break
    budget = float(input())
    while True:
        amount = float(input())
        saved_money += amount
        if saved_money >= budget:
            print(f"Going to {destination}!")
            saved_money = 0
            break

