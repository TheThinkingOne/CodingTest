import sys
sys.stdin = open('input.txt','r')

N = int(input())
P = list(map(int,input().split()))
sum = 0

while len(P) > 0:
    minVal = min(P)
    for i in range(N):
        if P[i] == minVal:
            sum += P[i] * len(P)
            P.remove(minVal)
            N -= 1
            break

print(sum)