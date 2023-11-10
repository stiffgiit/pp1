def f(amount_to_pay):
    #check if the input is a non negative integer
    if not isinstance(amount_to_pay, int) or amount_to_pay < 0:
        return "Invalid input"
    
    coins_count = 0
    
    #calculate the amount of 5 PLN coins
    
    coins_count += amount_to_pay // 5
    amount_to_pay %= 5
    
    #calculate the amount of 2pln coins
    
    coins_count += amount_to_pay // 2
    amount_to_pay %= 2
    
    #the remaining amount can be covered with 1 pln coins
    coins_count += amount_to_pay
    
    return coins_count

print(f(23))
print(f(8))
print(f(2))