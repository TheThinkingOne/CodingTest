import sys
sys.stdin = open('input.txt','r')

N = int(input())
count = 0
NList = []
for i in range(1,N+1):
    if N % i == 0:
        NList.append(i)

#print(NList)
for i in range(len(NList)):
    for j in range(len(NList)):
        if NList[i] * NList[j] == N:
            count += 1

print(count)
