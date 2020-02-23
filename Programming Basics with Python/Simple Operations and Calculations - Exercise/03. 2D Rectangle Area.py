x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

width = abs(x1 - x2)

height = abs(y1 - y2)

area = width * height

peremeter = 2 * (width + height)

print(f'{area:.2f}')

print(f'{peremeter:.2f}')
