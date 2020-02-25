goal = 10000
steps = 0


while steps < goal: 
    entered = input()
    if entered == "Going home":
        entered = input()
        steps += int(entered)
        break
    else:
        steps += int(entered)
        
    

if steps >= goal:
    print('Goal reached! Good job!')
else:
    print(f'{goal - steps} more steps to reach goal.')

