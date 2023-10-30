import re
def main():
    password = input("Enter password: ")
    if (len(password) >= 8):
        print("Password is valid: True")
    else: 
        print("Password is valid: False")
        
if __name__ == "__main__":
    main()