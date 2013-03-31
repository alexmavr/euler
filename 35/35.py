from math import ceil
from math import sqrt
from collections import deque
import numpy

def is_prime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    for i in range(2, int(ceil(sqrt(num))) + 1):
        if num % i == 0:
            return False
    return True

def list_to_int(numL):
    return int(''.join(map(str, numL)))

def int_to_list(num):
    return [int(i) for i in str(num)]

def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = numpy.ones(n/3 + (n%6==2), dtype=numpy.bool)
    for i in xrange(1,int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k/3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)/3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]

def main():
    primes =  primesfrom2to(1000000)
    counter = 0
    for i in primes:
        L = deque(int_to_list(i))
        flag = True
        for j in range(1,len(L)):
            L.rotate()
            if not is_prime(list_to_int(L)):
                flag = False
        if flag:
            counter += 1
    print counter

if __name__=="__main__":
    main()
