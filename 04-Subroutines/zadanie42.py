def f(number1, number2, number3):
    smol = min(number1, number2, number3)
    huge = max(number1, number2, number3)
    difer = huge - smol
    return difer
    
print(f(7,4,9))
print(f(2,12,8))