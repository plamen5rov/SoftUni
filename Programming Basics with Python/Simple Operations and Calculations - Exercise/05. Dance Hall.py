from math import floor

length = float(input())

width = float(input())

wardrobe_side = float(input())

hall_area = length * width

bench_area = hall_area / 10

dance_area = hall_area - bench_area - pow(wardrobe_side, 2)

dancers = floor(dance_area / 0.7040)

print(dancers)
