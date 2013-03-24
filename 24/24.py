from itertools import permutations

def main():
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    perms = list(permutations(digits))
    perms.sort()
    print perms[999999]

if __name__=="__main__":
    main()
