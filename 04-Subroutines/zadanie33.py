def f(n):
    if not isinstance(n,int) or n < 1:
        return "invalid input"
    
    count = "*/" * (n-1) + "*"
    
    return count

print(f(6))