age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

toys = 0
money = 0
sum_money = 0
taken_money = 0

for i in range (1, age + 1):
    if i % 2 != 0:
        toys += 1
    else:
        money += 10
        taken_money += 1
        sum_money += money

total_money = sum_money + (toys * toy_price) - taken_money

if total_money >= washing_machine_price:
    print(f'Yes! {total_money - washing_machine_price:.2f}')
else:
    print(f'No! {washing_machine_price - total_money:.2f}')
