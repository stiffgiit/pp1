def different(n1,n2,n3):
    
    if n1 != n2 and n2 != n3 and n3 != n2:
        return false
    else:
        return true 
        
n1 = int(input("Enter first number:  "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))
if different(n1,n2,n3):
    print(f"numbers {n1}, {n2}, {n3} are different ")