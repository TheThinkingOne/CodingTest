import sys
sys.stdin = open('input.txt','r')

N = int(input())
AList = list(map(int,input().split()))
BList = list(map(int,input().split()))

sumOfLists = 0

while len(AList) != 0 and len(BList) != 0:
    val1 = min(AList) * max(BList)
    val2 = max(AList) * min(BList)
    sumOfLists += val1
    sumOfLists += val2
    AList.remove(min(AList))
    AList.remove(max(AList))
    BList.remove(min(BList))
    BList.remove(max(BList))

rest = AList[0] * BList[0]