import math

def is_prime(next):
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while math.pow(i, 2) <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w

    return True

s = 0
max = 2000000

for n in range(2, max-1):
    if is_prime(n):
        s += n

print(s)
