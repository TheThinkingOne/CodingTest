import sys
sys.stdin = open('input.txt','r')

TC = int(input())

for i in range(TC):
    x, y, z = map(int,input().split())
    k = abs((2*y-x-z) / 2)
    print(f"#{i+1} {k}")