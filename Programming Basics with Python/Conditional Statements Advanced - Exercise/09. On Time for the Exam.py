hour_of_exam = int(input())
minutes_of_exam = int(input())
hour_of_arrival = int(input())
minute_of_arrival = int(input())
 
 
if hour_of_exam == 0:
    hour_of_exam += 24
 
 
total_min_of_exam = (hour_of_exam * 60) + minutes_of_exam
total_min_of_arr = (hour_of_arrival * 60) + minute_of_arrival
total_min_dif = total_min_of_exam - total_min_of_arr
 
if total_min_dif == 0:
    print('On time')
elif 0 < total_min_dif <= 30:
    print('On time')
    print(f'{total_min_dif} minutes before the start')
elif 30 < total_min_dif < 60:
    print('Early')
    print(f'{total_min_dif} minutes before the start')
elif total_min_dif >= 60:
    hours = total_min_dif // 60
    minutes = total_min_dif % 60
    print('Early')
    print(f'{hours}:{minutes:02d} hours before the start')
elif total_min_dif > -60:
    total_min_dif *= -1
    print('Late')
    print(f'{total_min_dif} minutes after the start')
elif total_min_dif <= -60:
    total_min_dif *= -1
    hours = total_min_dif // 60
    minutes = total_min_dif % 60
    print('Late')
    print(f'{hours}:{minutes:02d} hours after the  start')
