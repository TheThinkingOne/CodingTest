import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
for i in range(N):
    Data = list(map(int,input().split()))
    for y in range(-10000,10001):
        for x in range(-10000,10001):
            count = 0
            if Data[2] ** 2 - int(x) ** 2 == Data[5] ** 2 - int(y) ** 2:
                count += 1
                print(count)
