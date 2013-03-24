from __future__ import division

def list_to_int(numL):
    return int(''.join(map(str, numL)))

def int_to_list(num):
    return [int(i) for i in str(num)]

def curious():
    curious = []
    for numerator in range(10, 100):
        for denominator in range(numerator, 100):
            numL = int_to_list(numerator)
            denL = int_to_list(denominator)
            for i in numL:
                if i in denL:
                    numL.remove(i)
                    denL.remove(i)
                    if i != 0 and denL[0] != 0 and numL[0]/denL[0]!=1.0 and \
                                    numL[0]/denL[0] == numerator/denominator:
                        curious.append((numerator, denominator))
    return curious

def main():
    to_prod = curious()
    num_tot = 1
    den_tot = 1
    for num, den in to_prod:
        num_tot *= num
        den_tot *= den
    print "Final product: " + str(num_tot) + " / " + str(den_tot)

if __name__=="__main__":
    main()
