string = (input())
n = len(string)
aggregated = 0
for x in range(0, n):
    char = string[x]

    if char == 'a':
        aggregated += 1
    elif char == 'e':
        aggregated += 2
    elif char == 'i':
        aggregated += 3
    elif char == 'o':
        aggregated += 4
    elif char == 'u':
        aggregated += 5
print (aggregated)
