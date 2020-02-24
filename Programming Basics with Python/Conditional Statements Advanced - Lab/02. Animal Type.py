dog_type = input()

if dog_type == 'dog':
    message = 'mammal'
elif (dog_type == 'crocodile') or (dog_type == 'snake') or (dog_type == 'tortoise'):
    message = 'reptile'
else:
    message = 'unknown'
    
print(message)
