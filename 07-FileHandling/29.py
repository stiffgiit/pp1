import re

with open("griffin.txt", "r") as file:
    text = file.read()
    lolo = re.findall(r"\d\.\d", text)
    
    aa = [float(l) for l in lolo]
    
    avg = sum(aa)/len(aa)
    print(round(avg, 2))