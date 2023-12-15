import re

with open("hello.txt", "r") as file:
    text = file.read()
    a = re.findall(r"\b\w{6,}\b", text)
    for word in a:
        print(word)