from math import floor

player = input()
number_of_games = int(input())

volleyball_count = 0
volleyball_points = 0

tennis_count = 0
tennis_points = 0

badminton_count = 0
badminton_points = 0

for i in range(1, number_of_games + 1):

    game = input()
    points = float(input())

    if game == "volleyball":
        volleyball_count += 1
        volleyball_points += points * 1.07
    elif game == "tennis":
        tennis_count += 1
        tennis_points += points * 1.05
    elif game == "badminton":
        badminton_count += 1
        badminton_points += points * 1.02

total_points = floor(volleyball_points + tennis_points + badminton_points)

volleyball_points = volleyball_points / volleyball_count

tennis_count = tennis_points / tennis_count

badminton_points = badminton_points / badminton_count



if volleyball_points > 75 and tennis_points > 75 and badminton_points > 75:
    print(f"Congratulations, {player}! You won the cruise games with {total_points} points.")
else:
    print(f"Sorry, {player}, you lost. Your points are only {total_points}.")
