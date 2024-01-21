def primeList(maxval):
    primes = [2, 3, 5, 7, 11]
    current = 13
    while current <= maxval:
        for x in primes:
            isPrime = True
            if x*x > current:
                break
            if current % x == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(current)
        current = current + 2
    return primes

