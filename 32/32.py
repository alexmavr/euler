from itertools import permutations

def list_to_int(numL):
    return int(''.join(map(str, numL)))

def main():
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    s = 0
    prods = []
    for i in permutations(digits, 9):
        for mul_len in range(1,3):
            multiplicand = list_to_int(i[0:mul_len])
            multiplier = list_to_int(i[mul_len:5])
            res = list_to_int(i[5:9])
            if multiplicand * multiplier == res and res not in prods:
                print "found "+ str(multiplicand) + " * " + str(multiplier) + " = " + str(res)
                prods.append(res)
                s += res
    print s

if __name__=="__main__":
    main()
