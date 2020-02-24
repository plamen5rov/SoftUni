import math

n = int(input())

leftSum = 0

rightSum = 0

for i in range(1, n + 1):
    leftSum += int(input())

for i in range(1, n + 1):
    rightSum += int(input())

if leftSum == rightSum:
    print(f'Yes, sum = {leftSum}')
else:
    diff = abs(leftSum - rightSum)
    print(f'No, diff = {diff}')
