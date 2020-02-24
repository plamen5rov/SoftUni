length = int(input())

width = int(input())

height = int(input())

per_cent = float(input()) * 0.01

volume = length * width * height

litres = volume * 0.001

solution = litres * (1 - per_cent)

print(f"{solution:.3f}")
