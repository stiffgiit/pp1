def coupon():
    for row in range(7):
        for col in range(7):
            number = row + 1 + col * 7
            print(f"{number:2}", end=" ")
        print()
        
if __name__ == "__main__":
    coupon()