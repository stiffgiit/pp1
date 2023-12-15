import re

text = "To be, or not to be, that is the question"

vowels = re.findall(r"[aeiou]", text, flags=re.IGNORECASE)

ala = len(vowels)

print("Vowels:", ala)