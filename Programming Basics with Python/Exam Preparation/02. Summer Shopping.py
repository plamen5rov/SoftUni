budget = int(input())

towel = float(input())

discount = int(input()) / 100

umbrella = towel * 2 / 3

flip_flops = umbrella * 0.75

bag = (flip_flops + towel) / 3

spending = (towel + umbrella + flip_flops + bag) * (1 - discount)

if budget >= spending:
    print(f"Annie's sum is {spending:.2f} lv. She has {budget - spending:.2f} lv. left.")
else:
    print(f"Annie's sum is {spending:.2f} lv. She needs {spending - budget:.2f} lv. more.")
