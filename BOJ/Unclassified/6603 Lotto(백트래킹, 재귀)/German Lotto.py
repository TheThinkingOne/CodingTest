import sys
sys.stdin = open('input.txt', 'r')

Stack = []
Data = list(map(int, sys.stdin.readline().split()))
K = Data[0]
if K != 0:
    for i in range(1, K+1):
        Stack.append(i)
        for j in range(len(Stack) -1, -1, -1):
            Stack.pop(j)
            Stack.sort()
            print(Stack)




