import sys
sys.stdin = open('input.txt','r')

N = int(input())
P = list(map(int,input().split()))
sum = 0

while len(P) > 0:
    minVal = min(P)
    minIndex = P.index(min(P))

    sum += sum + minVal * minIndex
    P.remove(min(P))

print(sum)


