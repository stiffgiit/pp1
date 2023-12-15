with open("example.txt", "r", encoding="utf-8") as file:
    count = 0
    for line in file:
        print(line)
        count += 1
        if count%5 == 0:
            enter = input("Press enter")
            continue
        elif count == 30:
            quit()