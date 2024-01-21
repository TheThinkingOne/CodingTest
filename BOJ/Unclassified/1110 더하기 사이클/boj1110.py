import sys
sys.stdin = open('input.txt','r')

N = list(map(int,input()))
print(N)
next = 0
# print(len(N))

if len(N) == 1:
    N[0] *= 10
    next = N[0]
elif len(N) == 2:
    next = N[0] + N[1]
