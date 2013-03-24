def main():
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = [[0]*201 for j in range(0, len(coins)+1)]

    ways[0][0] = 1
    for i in xrange(0, len(coins)):
        for j in xrange(0,201):
            for k in xrange(j, 201, coins[i]):
                ways[i+1][k] += ways[i][j]
    print ways[8][200]

if __name__=="__main__":
    main()
