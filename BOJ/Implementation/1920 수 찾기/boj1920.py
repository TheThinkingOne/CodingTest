import sys
sys.stdin = open('input.txt','r')

N = int(input())
num1 = input().split()
M = int(input())
num2 = input().split()

for i in range(M):
    count = 0
    for j in range(N):
        if num2[i] == num1[j]:
            count += 1
            break
    print(count)




