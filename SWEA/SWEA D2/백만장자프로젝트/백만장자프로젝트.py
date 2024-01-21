import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for i in range(T):
    days = int(input()) #days = 3,3,5
    price = list(map(int, input().split()))
    benefit = 0
    lastDayPrice = price[days-1]
    for j in range(days-2,-1,-1): #j=1,0 또는 j=3,2,1,0 의 순서로 돌아감
        if lastDayPrice >= price[j]:
            benefit += (lastDayPrice - price[j])
        else:
            lastDayPrice = price[j]
    print(f"#{i+1} {benefit}")
    # for j in range(days):
    #     if (price[j] + price[j+1]) > price[j+2]:
    #         benefit += (price[j+2]*2 - price[j] - price[j+1])
    #     else:
    #         benefit += 0
    #     print(benefit)
