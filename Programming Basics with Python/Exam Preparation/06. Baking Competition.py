players = int(input())
bakery = 0
personal_sum = 0
total_sum = 0


for line in range(players):
    name = input()

    cookies = 0
    cakes = 0
    waffles = 0
    command = input()

    while command != "Stop baking!":

        baked = command
        number_baked = int(input())
        bakery += number_baked
        if baked == "cookies":
            cookies += number_baked
        elif baked == "cakes":
            cakes += number_baked
        elif baked == "waffles":
            waffles += number_baked
        command = input()

    print(f"{name} baked {cookies} cookies, {cakes} cakes and {waffles} waffles.")

    personal_sum = cookies * 1.50 + cakes * 7.80 + waffles * 2.30

    total_sum += personal_sum

print(f"All bakery sold: {bakery}")
print(f"Total sum for charity: {total_sum:.2f} lv.")
