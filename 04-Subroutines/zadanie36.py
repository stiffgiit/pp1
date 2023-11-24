def f(detector):
    
    count = 0
    max_count = 0
    
    for char in detector:
        if  char == "+":
            count += 1
            max_count = max(max_count,count)
        elif char == "-":
            count -= 1
            
    return max_count >= 3

print(f("+-+++-+---"))
print(f("+-+-+-+-"))
print(f("+-++-+--"))
print(f("+-++-++-+---"))