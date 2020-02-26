n = int(input())
sum_grade = 0
average_grade = 0
total_average = 0
counter = 0

command = input()

while command != "Finish":
    presentation = command
    counter += 1
    for i in range(n):
        grade = float(input())
        sum_grade += grade
    average_grade = sum_grade / n
    total_average += average_grade
    print(f'{presentation} - {average_grade:.2f}.')
    sum_grade = 0
    command = input()

total_average = total_average / counter
print(f"Student's final assessment is {total_average:.2f}.")
