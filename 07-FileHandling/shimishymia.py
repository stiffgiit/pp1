import re

with open("lolek.txt", "r") as file:
    hehe = file.read()
    a = re.findall('Note \d - ([^\n]*)', hehe)
    print(a)