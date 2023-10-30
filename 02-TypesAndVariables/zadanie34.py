import re
def main():
    speed = float(input("Enter speed: "))
    if speed >= 40 and speed <= 140:
        print("Speed is valid: true")
    else:
        print("Speed is valid: False")
        
if __name__ == "__main__":
    main()