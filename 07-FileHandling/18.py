with open('countries.txt', 'r') as firstfile, open("pusty.txt", "a") as secondfile:
    for line in firstfile:
        
        secondfile.write(line)

