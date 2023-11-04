def coins(amount):
    coin = [5, 2, 1]
    counts = [0, 0, 0]
    
    for i in range(len(coin)):
        counts[i] = amount // coin[i]
        amount %= coin[i]
        
    return counts


amount = int(input("Enter the amount in PLN: "))

if amount <= 0:
    print("Please enter a positive amount.")
else:
    counts = coins(amount)
    print(f"The amount of PLN {amount} in coins: ")
    print(f"5 zł - {counts[0]}")
    print(f"2 zł - {counts[1]}")
    print(f"1 zł - {counts[2]}")