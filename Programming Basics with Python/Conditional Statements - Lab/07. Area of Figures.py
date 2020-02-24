from math import pi

figure = input()
dimension = float(input())

if figure == "square":
    area = dimension * dimension
    
elif figure == "rectangle":
    sideB = float(input())
    area = dimension * sideB
    
elif figure == "circle":
    area = pi * dimension ** 2
    
elif figure == "triangle":
    hight = float(input())
    area = dimension * hight / 2
    
print (f'{area:.3f}')
