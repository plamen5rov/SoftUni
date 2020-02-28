monthly_income = float(input())

months = int(input())

expenses = float(input())

reserve = monthly_income * 0.30

money_left = monthly_income - expenses - reserve

saved_money = months * money_left

percentage = money_left / monthly_income * 100

print(f'She can save {percentage:.2f}%')

print(f'{saved_money:.2f}')
