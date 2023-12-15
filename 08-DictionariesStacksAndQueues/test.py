import json

with open("idk.txt", "r", encoding="utf-8") as file:
    lol = json.load(file)
    file.close()
    
    a = lol["debug"]
    print(a)