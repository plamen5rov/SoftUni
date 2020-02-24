num = int(input())
sum_odd = 0
sum_even = 0
max_odd_num = -9999999
max_even_num = -9999999
min_odd_num = 99999999
min_even_num = 99999999

for n in range(1,num + 1):
    current_num = float(input())

    if n % 2 == 0:
        sum_even += current_num
        if current_num >= max_even_num:
            max_even_num = current_num
        if current_num <= min_even_num:
            min_even_num = current_num
    else:
        sum_odd += current_num
        if current_num >= max_odd_num:
            max_odd_num = current_num
        if current_num <= min_odd_num:
            min_odd_num = current_num

print(f"OddSum={sum_odd:.2f},")

if min_odd_num == 99999999:
    print("OddMin=No,")
else:
    print(f"OddMin={min_odd_num:.2f},")

if max_odd_num == -9999999:
    print(f"OddMax=No,")
else:
    print(f"OddMax={max_odd_num:.2f},")

print(f"EvenSum={sum_even:.2f},")

if min_even_num == 99999999:
    print("EvenMin=No,")
else:
    print(f"EvenMin={min_even_num:.2f},")
if max_even_num == -9999999:
    print("EvenMax=No")
else:
    print(f"EvenMax={max_even_num:.2f}")
