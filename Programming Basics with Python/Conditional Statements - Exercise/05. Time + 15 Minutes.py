start_hour = int(input())
start_minutes = int(input())

time_in_minutes = start_hour * 60 + start_minutes + 15

hours = time_in_minutes // 60
minutes = time_in_minutes % 60

if hours > 23:
    hours = hours - 24

if minutes < 9:
    print(f"{hours}:0{minutes}")
else:
    print(f"{hours}:{minutes}")
