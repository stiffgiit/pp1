enter = input("File name: ")

with open(enter, "r", encoding="utf-8") as file:
    count = 0
    for line in file:
        count += 1
    print("Number of lines: ", count)