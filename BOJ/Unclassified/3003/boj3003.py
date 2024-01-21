import sys
sys.stdin = open('input.txt', 'r')

chessPieces = list(map(int,input().split()))
neededPieces = [1, 1, 2, 2, 2, 8]

for i in range(len(chessPieces)):
    neededPieces[i] -= chessPieces[i]
    print(neededPieces[i],end=' ')