def f(x,y):
    if not isinstance(x,int) or not isinstance(y,int) or x > y:
        return "invalid input"
    
    #initialize the count of negative even numbers
    count = 0
    
    for num in range(x,y+1):
        if num < 0 and num%2 == 0:
            count += 1
            
    return count


print(f(-7,8))