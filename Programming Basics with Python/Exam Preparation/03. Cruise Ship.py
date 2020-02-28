cruise_type = input()

cabin_type = input()

nights = int(input())

discount = 1

if nights > 7:
    discount = 1 - 0.25

per_night_price = 0

if cruise_type == "Mediterranean":
    if cabin_type == "standard cabin":
        per_night_price = 27.50
    elif cabin_type == "cabin with balcony":
        per_night_price = 30.20
    elif cabin_type == "apartment":
        per_night_price = 40.50

elif cruise_type == "Adriatic":
    if cabin_type == "standard cabin":
        per_night_price = 22.99
    elif cabin_type == "cabin with balcony":
        per_night_price = 25.00
    elif cabin_type == "apartment":
        per_night_price = 34.99

elif cruise_type == "Aegean":
    if cabin_type == "standard cabin":
        per_night_price = 23.00
    elif cabin_type == "cabin with balcony":
        per_night_price = 26.60
    elif cabin_type == "apartment":
        per_night_price = 39.80

total_price = nights * per_night_price * discount * 4

print(f"Annie's holiday in the {cruise_type} sea costs {total_price:.2f} lv.")
