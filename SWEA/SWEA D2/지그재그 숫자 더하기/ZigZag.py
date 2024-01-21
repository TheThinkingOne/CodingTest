import sys
sys.stdin = open('input.txt','r')

T = int(input())
for i in range(T):
    num = int(input())
    Result = 0
    for j in range(1,num+1):
        if j % 2 == 0:
            j = -j
        Result += j
    print(f"#{i+1} {Result}")