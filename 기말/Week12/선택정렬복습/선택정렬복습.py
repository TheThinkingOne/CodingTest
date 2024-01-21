import sys
sys.stdin = open('input.txt', 'r')

Data = list(map(int,input().split()))

for here in range(1, len(Data)):
    key = Data[here]
    where = here-1
    while key < Data[where] and where>=0:
        Data[where+1] = Data[where]
        where-=1
    Data[where+1] = key

print(Data)