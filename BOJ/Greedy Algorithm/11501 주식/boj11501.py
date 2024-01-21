import sys
sys.stdin = open('input.txt','r')

T = int(input())
for i in range(T):
    days = int(input())
    stock = list(map(int,input().split()))
    totalBenefit = 0

    # while len(stock) != 0:
    #     for j in range(days):
    #         if stock[0] == max(stock):
    #             totalBenefit = 0
    #             break
    #         elif stock[j] == max(stock):
    #             totalBenefit += max(stock) * j
    #             for k in range(j):
    #                 totalBenefit -= stock[k]
    #                 stock.remove(stock[k])
    #             stock.remove(max(stock))
    #
    # print(totalBenefit)
    while stock:
        maxPrice = max(stock)
        maxIndex = stock.index(maxPrice)

        # if maxIndex == 0:
        #     totalBenefit = 0
        #     break

        totalBenefit += maxPrice * maxIndex
        totalBenefit -= sum(stock[0:maxIndex])
        stock = stock[maxIndex + 1: days]

    print(totalBenefit)



