name = "Dominik Kawula"
univeristy = "Krakow Univeristy of Economics"
field = "Applied Informatics"

with open("student.txt", "w", encoding="utf-8") as file:
    file.write(name+'\n')
    file.write(univeristy+'\n')
    file.write(field+'\n')
file.close()