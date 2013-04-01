
def list_to_int(numL):
    return int(''.join(map(str, numL)))

def int_to_list(num):
    return [int(i) for i in str(num)]

def is_pandigital(num):
    return len(str(num)) == 9 and set(str(num)) == set("123456789")

def main():
    max_pand = 123456789
    for i in range(1, 10000):
        j = 1
        s = []
        while len(s) < 9:
            for k in int_to_list(i * j):
                s.append(k)
            j = j + 1
        if is_pandigital(list_to_int(s)) and list_to_int(s) > max_pand:
            max_pand=list_to_int(s)
    print max_pand

if __name__=="__main__":
    main()
