def f(n):
    if n <= 0:
        return "invalid input, n should be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return f(n-1) + f(n-2)
    
print(f(5))
print(f(9))