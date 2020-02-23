whisky_price = float(input())

beer = float(input())

wine = float(input())

rakya = float(input())

whisky = float(input())

payment_whisky = whisky * whisky_price

payment_rakya = rakya * (whisky_price * 0.5)

payment_wine = wine * ((whisky_price * 0.5) - ((whisky_price * 0.5)* 0.4))

payment_beer = beer * ((whisky_price * 0.5) - ((whisky_price * 0.5)* 0.8))

money = payment_beer + payment_rakya + payment_whisky + payment_wine

print(f'{money:.2f}')
