with open('movies.txt', 'r', encoding="utf-8") as file:
    for line in file:
        print(line, end="")
    file.close()