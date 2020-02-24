age = float(input())
sex = input()
result = ''

if sex == 'm':
    if age >= 16:
        result = 'Mr.'
    else:
        result = 'Master'
elif sex == 'f':
    if age >= 16:
        result = 'Ms.'
    else:
        result = 'Miss'
print (result)
