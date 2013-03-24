# only for capitals
def char_num(x):
    return ord(x) - 64

def main():
    f = open("names.txt", 'r')
    names = f.read()[1:-1].split("\",\"")
    total_sum = 0
    for i,j in enumerate(sorted(names)):
        summ = 0
        for char in j:
            summ += char_num(char)
        total_sum += summ * (i+1)
    print total_sum

if __name__=="__main__":
    main()
