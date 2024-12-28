def find_primes(n):
    if n < 2:
        return []

    # Create a boolean array "prime[0..n]" and initialize
    # all entries as True. A value in prime[i] will
    # finally be False if i is Not a prime, else True.
    prime = [True for _ in range(n + 1)]

    p = 2

    while p * p <= n:
        # If prime[p] is not changed, then it is a prime
        if prime[p]:
            # Updating all multiples of p to not be prime
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    # Collecting all prime numbers
    primes = [p for p in range(2, n + 1) if prime[p]]
    return primes


# Example usage
n = 30
print(f"Prime numbers less than or equal to {n}: {find_primes(n)}")
