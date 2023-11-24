def f(name):
    
    output = name[0]
    
    for i in range(1, len(name)):
        if name[i-1] == ' ':
            output += name[i]
            
    return output

print(f('Internet of Things'))
print(f('For Your Information'))
print(f("Python"))