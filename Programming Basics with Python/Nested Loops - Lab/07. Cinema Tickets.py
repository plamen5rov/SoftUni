student = 0
standard = 0
kid = 0
all_tickets = 0
tickets_film = 0

name = input()

while name != "Finish":
    film_name = name
    capacity = int(input())
    tickets_film = 0
    movie_type = input()


    while movie_type != "End":


        if movie_type == "student":
            student += 1
        elif movie_type == "standard":
            standard += 1
        elif movie_type == "kid":
            kid += 1
        tickets_film += 1
        all_tickets += 1

        if tickets_film >= capacity:
            break
        movie_type = input()

    percentage = tickets_film / capacity * 100
    print(f'{film_name} - {percentage:.2f}% full.')
    name = input()

if name == "Finish":
    print(f'Total tickets: {all_tickets}')
    percentage_students = student / all_tickets * 100
    percentage_standard = standard / all_tickets * 100
    percentage_kids = kid / all_tickets * 100

    print(f'{percentage_students:.2f}% student tickets.')
    print(f'{percentage_standard:.2f}% standard tickets.')
    print(f'{percentage_kids:.2f}% kids tickets.')
