with open('shopping.txt', 'w', encoding="utf-8") as file:
    read = True
    counter = 0
    while read:
        product = input("Enter product name: ")
        if product != "":
            counter += 1
            file.write(f"{counter}. {product} "+ "\n")
        else:
            read = False
    file.close()