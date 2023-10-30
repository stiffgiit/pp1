def card():
    number = input("Enter credit card number: ")
    print("Card number: {} {} {} {}".format(number[:4],number[4:8],number[8:12],number[12:16]))
card()  