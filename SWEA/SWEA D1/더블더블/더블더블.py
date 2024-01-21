import sys
sys.stdin = open('input.txt', 'r')
T = int(input())

for i in range(0,T+1):
    k = 2**i
    print(k, end=' ')


