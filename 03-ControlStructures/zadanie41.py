pin = '0805'
max = 3
attemp = 0


while attemp < max:
    enter = input("Enter the PIN code: ")
    
    
    if enter == pin:
        print("PIN code is correct. Payment card is unlocked.")
        break
    else:
        print("Incorrect...")
        attemp += 1
        

if attemp == max:
    print("Sorry, your payment card has been blocked.")