numbers = int(input())
sum_all = 0

max_num = -9999999

for n in range(1, numbers + 1):
    current_num = int(input())
    sum_all += current_num

    if current_num > max_num:
        max_num = current_num

final_sum = sum_all - max_num
if max_num == final_sum:
    print('Yes')
    print(f'Sum = {max_num}')

else:
    print('No')
    diff = abs(max_num - final_sum)
    print(f'Diff = {diff}')
