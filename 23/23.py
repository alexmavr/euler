from itertools import combinations
from abundants import abundants

def is_abundant(x):
    divisor_sum = 0
    for j in xrange(2, (x/2 + 1)):
        if x % j == 0:
            divisor_sum += j
    if divisor_sum > x:
        return True
    return False


def main():
    remainder = range(1, 28124)
    print "generated remainder"
    for i,j in combinations(abundants, 2):
        if (i+j) in remainder:
            remainder.remove(i+j)
    print sum(remainder)

if __name__=="__main__":
    main()
