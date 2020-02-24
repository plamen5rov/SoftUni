from math import pi

figure = input()
dimension = float(input())

if figure == "square":
    area = dimension * dimension
    print (f'{area:.3f}')
elif figure == "rectangle":
    sideB = float(input())
    area = dimension * sideB
    print(f'{area:.3f}')
elif figure == "circle":
    area = pi * dimension ** 2
    print(f'{area:.3f}')
elif figure == "triangle":
    hight = float(input())
    area = dimension * hight / 2
    print(f'{area:.3f}')

