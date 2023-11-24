def f(password):
    if len(set(password)) >= 6 and len(password) >= 6 and len(set(password)) == len(password):
        return True
    else:
        return False
    
print(f("ax15"))
print(f("book123"))
print(f("A2water3"))
print(f("qwerty"))
print(f(""))