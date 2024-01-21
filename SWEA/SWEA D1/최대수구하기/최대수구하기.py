import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for i in range(T):
    maxVal = 0
    Data = list(map(int, input().split()))
    for j in range(len(Data)):
        if Data[j] > maxVal:
            maxVal = Data[j]
    print(f"#{i+1} {maxVal}")