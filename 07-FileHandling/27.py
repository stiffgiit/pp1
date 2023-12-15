import re

text = "To be, or not to be, that is the question"

lol = re.findall(r'\b\w+\b', text)

total_words = len(lol)
print(total_words)