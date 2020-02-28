initial_points = int(input())

points = initial_points

moves = 0

while points > 0:
    section = input()
    moves += 1
    if section == "bullseye":
        print(f"Congratulations! You won the game with a bullseye in {moves} moves!")
        break
    else:
        current_points = int(input())

        if section == "number section":
            points -= current_points
        elif section == "double ring":
            points -= current_points * 2
        elif section == "triple ring":
            points -= current_points * 3


if points == 0:
    print(f"Congratulations! You won the game in {moves} moves!")


elif points < 0:
    points = abs(points)
    print(f"Sorry, you lost. Score difference: {points}.")

