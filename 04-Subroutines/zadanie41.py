def f(n):
    
    primes = [2]
    candidate = 3
    
    while len(primes) < n:
        if all(candidate % prime != 0 for prime in primes):
            primes.append(candidate)
        candidate += 2
    return primes[-1]

print(f(1))
print(f(5))