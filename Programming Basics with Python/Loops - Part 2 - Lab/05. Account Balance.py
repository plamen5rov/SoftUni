payments = int(input())
count = 1
total_sum = 0

while count <= payments:
    payment_sum = float(input())
    if payment_sum < 0:
        print('Invalid operation!')
        break
    else:
        print(f'Increase: {payment_sum:.2f}')
        total_sum += payment_sum
        count += 1


print(f'Total: {total_sum:.2f}')   
