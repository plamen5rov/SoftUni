screening_type = input()

rows = int(input())

columns = int(input())

income = 0

chairs = rows * columns

if screening_type == 'Premiere':
    income = chairs * 12.00
elif screening_type == 'Normal':
    income = chairs * 7.50
elif screening_type == 'Discount':
    income = chairs * 5.00

print(f"{income:.2f}")
