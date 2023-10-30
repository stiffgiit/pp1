import random

def roll():
    return random.randint(1,6)
def main():
    roll1 = roll()
    int(input("Enter a number : "))
    if roll1 == True:
        print("True")
    else: 
        print("False")  
        
if __name__ == "__main__":
    main()