import random

with open('pusty.txt', 'w') as file:
    for line in range(1,51):
        file.write(str(random.randrange(100,999)) + "\n")
        