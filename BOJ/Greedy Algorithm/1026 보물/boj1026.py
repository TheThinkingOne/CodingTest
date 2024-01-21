import sys
sys.stdin = open('input.txt','r')

N = int(input())
AList = list(map(int, input().split()))
BList = list(map(int, input().split()))

sumOfLists = 0

while len(AList) > 1 and len(BList) > 1:
    # "리스트 A의 길이가 1보다 크고, 그리고 리스트 B의 길이가 1보다 큰 동안에"
    # 두 리스트 중 하나라도 요소의 개수가 1 이하가 되면 while 루프는 종료됨.
    val1 = min(AList) * max(BList)
    val2 = max(AList) * min(BList)
    sumOfLists += val1
    sumOfLists += val2
    AList.remove(min(AList))
    AList.remove(max(AList))
    BList.remove(min(BList))
    BList.remove(max(BList))

if len(AList) == 1 and len(BList) == 1:
    rest = AList[0] * BList[0]
    print(sumOfLists + rest)
else:
    print(sumOfLists)


