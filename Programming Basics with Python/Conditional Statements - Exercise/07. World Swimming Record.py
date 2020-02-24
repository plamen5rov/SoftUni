import math

record_time = float(input())
distance = float(input())
time_4_1_minute = float(input())

delay_times = math.floor(distance / 15)

delay = delay_times * 12.5

time_in_seconds = distance * time_4_1_minute + delay

if time_in_seconds < record_time:
    print(f'Yes, he succeeded! The new world record is {time_in_seconds:.2f} seconds.')
else:
    print(f'No, he failed! He was {time_in_seconds - record_time:.2f} seconds slower.')
