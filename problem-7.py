def is_prime(num):
    prime_counter = 1
    for x in range(1, num):
        if num % x == 0:
            prime_counter += 1
        if prime_counter > 2:
            return False
    return True

primes = []
i = 1
p = 0
n = 10001


while p != n+1:
    if is_prime(i):
        primes.append(i)
        p += 1
    i += 1
        
print(primes[n])
