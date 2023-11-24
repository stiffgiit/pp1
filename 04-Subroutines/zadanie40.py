from collections import Counter

def f(number):
    digits_counter = Counter(str(number))
    repeated_sum = sum(int(digit) * count for digit, count in digits_counter.items() if count > 1)
    return repeated_sum

print(f(230335))
print(f(513553007))