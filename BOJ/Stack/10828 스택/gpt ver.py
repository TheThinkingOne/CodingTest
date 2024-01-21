import sys
sys.stdin = open('input.txt','r')

N = int(sys.stdin.readline().strip())  # Read N from the first line

Stack = []
top = -1
# top 변수를 이용해서 계산(인덱스 해서 하는것보다 시간복잡도 줄어듦)

for i in range(N):
    commandList = sys.stdin.readline().strip().split()
    command = commandList[0]

    if len(commandList) == 2:
        number = int(commandList[1])

    if command == 'push':
        Stack.append(number)
        top += 1

    elif command == 'pop':
        if top == -1:
            print(-1)
        else:
            print(Stack[top])
            Stack.pop()  # Simply pop without index since it's the last element
            top -= 1

    elif command == 'size':
        print(top + 1)

    elif command == 'empty':
        if top == -1:
            print(1)
        else:
            print(0)

    elif command == 'top':
        if top == -1:
            print(-1)
        else:
            print(Stack[top])

