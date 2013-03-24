def main():
    max_r = 6
    max_i = 7
    for i in range(12,999):
        past_rems = []
        rem = 1
        while rem != 0 and rem not in past_rems:
            past_rems.append(rem)
            rem *= 10
            while rem < i:
                rem *= 10
                past_rems.append(rem)
            rem %= i
            if rem in past_rems:
                l = len(past_rems)- past_rems.index(rem)
                print str(i) + " has " + str(l) + " recurring digits"
                if l > max_r:
                    max_r = l
                    max_i = i
    print str(max_i) + " is the max with " + str(max_r) + " recurring digits"

if __name__=="__main__":
    main()
