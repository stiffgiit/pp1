def phone():
    number = input("Enter your phone number: ")
    print("Phone number: {}-{}-{}".format(number[:3],number[3:6],number[6:]))
phone()