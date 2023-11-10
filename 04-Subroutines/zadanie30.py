def f(number, even):
    #i am checking if the input is a positive integer
    if not isinstance(number, int) or number < 0:
        return "invalid input"
    
    #converting the number to a string to iterate through digits 
    number_str = str(number)
    
    #initialize the sum of digits
    digit_sum_result = 0
    
    
    #iterating through each digit in the number 
    for digit_str in number_str:
        digit = int(digit_str)
        
        #checking if the digit is even or odd based on 'even' parameter 
        if even and digit%2 == 0 or not even and digit%2 != 0:
            digit_sum_result += digit
            
    return digit_sum_result


print(f(3124, True))
print(f(3124, False))