student = input()
grades_sum = 0
low_grades = 0
current_grade = 0

for i in range (1, 13):
    grade = float(input())
    current_grade +=1
    if grade < 4:
        low_grades += 1

    if low_grades <2:
        grades_sum += grade
    else:
        print(f'{student} has been excluded at {current_grade - 1} grade')
        break

average_grade = grades_sum / 12

if average_grade >= 4:
    print(f'{student} graduated. Average grade: {average_grade:.2f}')
