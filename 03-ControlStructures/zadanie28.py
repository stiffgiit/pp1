enter = input("Enter EAN-13 article number: ")
if (len(enter)) == 13 and enter.startswith('590'):
    print("Article number is correct")
    print("Article manufactured in Poland")
else:
    print("Article number incorrect")
    print("Article not manufactured in Poland")