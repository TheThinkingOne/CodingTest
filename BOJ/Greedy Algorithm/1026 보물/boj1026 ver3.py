import sys
sys.stdin = open('input.txt','r')

AList = []
BList = []

sumOfLists = 0

N = int(input())

for _ in range(N):
    A = int, input().split()
    B = int, input().split()
    AList.append(A)
    BList.append(B)
# AList = list(map(int,input().split()))
# BList = list(map(int,input().split()))


    while len(AList) != 1 and len(BList) != 0:
        val1 = min(AList) * max(BList)
        val2 = max(AList) * min(BList)
        sumOfLists += val1
        sumOfLists += val2
        AList.remove(min(AList))
        AList.remove(max(AList))
        BList.remove(min(BList))
        BList.remove(max(BList))

        rest = AList[0] * BList[0]