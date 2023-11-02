jacket = 40
und = 70
shoes = 20
rinse = 15
spin = 9
clothes = input("washing products: ") 
rinse1 = input("rinse = ") =='True'
spin1 = input("spin = ") =='True'


def clothes1(clothes, rinse_enabled, spin_enabled):
    if clothes == "jacket":
        time = jacket
        if rinse_enabled:
            time += rinse
        if spin_enabled:
            time += spin
    elif clothes == "und":
        time = und
        if rinse_enabled:
            time += rinse
        if spin_enabled:
            time += spin
    elif clothes == "shoes":
        time = shoes
        if rinse_enabled:
            time += rinse
        if spin_enabled:
            time += spin
    else:
        print("Invalid clothes")
    
    print(f"Total washing time for {clothes}: {time} minutes")
clothes1(clothes, rinse1, spin1)
    
        

    

    
    
        
