value = float(input())
input_metric = input()
output = input()

if input_metric == "mm":
    value /= 1000
elif input_metric == "cm":
    value /= 100

if output == "mm":
    value *= 1000
elif output == "cm":
    value *= 100

print(f'{value: .3f}')
