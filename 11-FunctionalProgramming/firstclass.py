#The first class functions can be:

#1. Assigned to variables

def square(x):
    return x**2

a = square

#2. Passed as argument to other functions

def apply(func, x):
    return func(x)

result = apply(square, 5)
print(result)

#3. Returned as values from other functions

def get_power_function(exponent):
    def power(x):
        return x**exponent
    return power


square_function = get_power_function(2)
result = square_function(4)