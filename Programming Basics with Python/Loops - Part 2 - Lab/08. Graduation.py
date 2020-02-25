student = input()
grades_sum = 0

for i in range (12):
    grade = float(input())
    grades_sum += grade

average_grade = grades_sum / 12

if average_grade >= 4:
    print(f'{student} graduated. Average grade: {average_grade:.2f}')
