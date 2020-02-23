tables = int(input())

table_length = float(input())

table_width = float(input())

covers_area = (table_length + 0.6) * (table_width + 0.6)

covers_price = covers_area * 7 * tables

kare_area = (table_length / 2) * (table_length / 2)

kare_price = kare_area * 9 * tables

price_usd = covers_price + kare_price

price_bgn = price_usd * 1.85

print(f'{price_usd:.2f} USD')

print(f'{price_bgn:.2f} BGN')
