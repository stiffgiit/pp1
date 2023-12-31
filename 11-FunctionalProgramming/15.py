text = "I completely agree with you"

a = text.split()

result = list(map(lambda x: len(x), a))
print(text)
print(f"No. of letters in words: {result}")