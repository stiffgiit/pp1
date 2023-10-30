import random 
def roll_dice():
    return random.randint(1,6)

def main():
    dice1 = roll_dice()
    dice2 = roll_dice()
    dice3 = roll_dice()
    
    sum = dice1 + dice2 + dice3
    
    print(f"Roll 1: {dice1}")
    print(f"Roll 2: {dice2}")
    print(f"Roll 3: {dice3}")
    print(f"Sum of dice rolled: {sum}")
    
if __name__ == "__main__":
    main()