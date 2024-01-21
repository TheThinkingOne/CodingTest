import sys
sys.stdin = open('input.txt','r')

N = int(input())
Stack = []
for i in range(N):
    commandList = list(map(str,input().split()))
    command = commandList[0]
    if len(commandList) == 2:
        number = commandList[1]

    if command == 'push':
        Stack.append(number)

    elif command == 'pop':
        if len(Stack) == 0: print(-1)
        else: print(Stack.pop(-1))

    elif command == 'size':
        print(len(Stack))

    elif command == 'empty':
        if len(Stack) == 0: print(1)
        else: print(0)

    elif command == 'top':
        if len(Stack) != 0: print(Stack[-1])
        else: print(-1)
