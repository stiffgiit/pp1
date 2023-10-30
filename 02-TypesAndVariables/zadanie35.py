import re

def main():
    tree = float(input("Enter tree circumference: "))
    if tree >= 50:
        print("Tree can be cut down: True")
    else:
        print("Tree can be cut down: False")
        
if __name__ == "__main__":
    main()
