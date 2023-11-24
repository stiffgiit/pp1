def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def generate_primes(n):
    prime_numbers = []
    number = 2
    while len(prime_numbers) < n:
        if is_prime(number):
            prime_numbers.append(number)
        number += 1
    return prime_numbers

def main():
    try:
        N = int(input("Enter the value of N: "))
        if N <= 0:
            print("Please enter a positive integer")
        else:
            prime_numbers = generate_primes(N)
            print("Prime numbers:", ' '.join(map(str, prime_numbers)))
    except ValueError:
        print("Invalid input. Please enter a valid integer")
        
        
if __name__ == "__main__":
    main()