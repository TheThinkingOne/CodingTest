import sys
sys.stdin = open('input.txt','r')
cashValueList = []
shareList = []
restList = []
result = 0

N, K = map(int,input().split())
for i in range(N):
    cashValue = int(input())
    cashValueList.append(cashValue)
# %:나머지, //:몫
#print(cashValueList)

def DividingCash(K):
    global result
    shareList = []
    restList = []
    while K != 0:
        for j in range(len(cashValueList)):
            share = K // cashValueList[j]
            rest = K % cashValueList[j]
            if rest != 0 and share != 0:
                shareList.append(share)
                result += min(shareList)
                restList.append(rest)
                newK = min(restList)
                if K == 0: break
                else : DividingCash(newK)

DividingCash(K)
print(result)



# print(K)
#
# print(shareList)
# print(restList)










