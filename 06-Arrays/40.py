import random

array = [random.randrange(1,999) for _ in range(8)]

stt = str(array)

a = stt.replace("[", "| ").replace("]", "|").replace(",", "| ")
print(len(a)*"-")
print(a)
print(len(a)*"-")

