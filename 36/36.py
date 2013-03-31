def int_to_list(num):
    return [int(i) for i in str(num)]

def is_palindromic(num):
    L = int_to_list(num)
    if list(reversed(L)) == L:
        return True
    else:
        return False

def main():
    s = 0
    for i in range(1, 1000000):
        if is_palindromic(i) and is_palindromic(int(bin(i)[2:])):
                s += i
    print s

if __name__=="__main__":
    main()
