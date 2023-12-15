import re

pattern = re.compile("[a-zA-Z\s]+")
print(pattern.search("Hello World"))