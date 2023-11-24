def f(expression):
    try:
        result = eval(expression)
        return result
    except:
        return "invalid expression"
    
    
print(f("2+3"))
print(f("3+8+1"))
print(f("2+3-4+5-0"))