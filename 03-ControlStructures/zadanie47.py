import random

def rand():
    for i in range(20):
        random_number = random.randint(5,10)
        print(random_number, end=" ")

if __name__ == "__main__":
    rand()