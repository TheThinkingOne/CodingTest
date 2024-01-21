import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(T):
    Data = list(map(int, input().split()))
    for i in range(len(Data)):
        if Data[i] == max(Data): Data[i] = max(Data)
    print(f"#{tc+1} {max(Data)}")

