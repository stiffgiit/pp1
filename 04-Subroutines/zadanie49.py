def f(dice):
    
    digits = [int(digit) for digit in str(dice)]
    
    frequent_digit = max(set(digits),key=digits.count)
    
    return frequent_digit


print(f("52955999900546"))