import sys
sys.stdin = open('input.txt', 'r')
N = int(sys.stdin.readline())
Stack = []
for i in range(N):
    Data = list(map(int, sys.stdin.readline().split()))
    if Data[0] == 1:
        Stack.append(Data[1])
    elif Data[0] == 2:
        if Stack:
            a = Stack.pop()
            print(a)
        else:
            print(-1)
    elif Data[0] == 3:
        print(len(Stack))
    elif Data[0] == 4:
        if Stack:
            print(0)
        else:
            print(1)
    elif Data[0] == 5:
        if Stack:
            print(Stack[-1])
        else:
            print(-1)

