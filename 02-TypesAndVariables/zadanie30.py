import random

def roll():
    return random.randint(1,6)
def main():
    dice1 = roll()
    print(f"Dice rolled: {dice1}")
    if dice1 == 1 or dice1 == 6:
        print("Special number: True")
    else:
        print("Special number: False")
        
if __name__ == "__main__":
    main()