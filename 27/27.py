from math import sqrt
from math import ceil

def isprime(x):
    if x < 0:
        return False
    for i in range(2, int(ceil(sqrt(x))) + 1):
        if x % i == 0:
            return False
    return True

def quad_primes(a,b):
    n = 0
    while isprime(n**2 + a * n + b):
        n += 1
    return n

def main():
    assert quad_primes(1,41) == 40
    assert quad_primes(-79,1601) == 80

    prime_max = 40
    maxa, maxb, = 1 , 41
    for a in range(-1000, 1001):
        for b in range(-1000,1001):
            if quad_primes(a, b) > prime_max:
                prime_max = quad_primes(a, b)
                maxa, maxb = a, b
    print maxa * maxb

if __name__=="__main__":
    main()
