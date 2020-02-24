import math

n = int(input())

oddSum = 0

evenSum = 0

for i in range(1, n + 1):
    num = int(input())
    if i % 2 == 0:
        evenSum += num
    else:
        oddSum += num

if oddSum == evenSum:
    print("Yes")
    print(f'Sum = {oddSum}')
else:
    diff = abs(oddSum - evenSum)
    print("No")
    print(f'Diff = {diff}')
