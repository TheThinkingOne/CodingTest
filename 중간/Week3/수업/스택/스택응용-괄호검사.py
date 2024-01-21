import sys
sys.stdin = open('input.txt', 'r')

stack = []
Data= input()
ans = 0

for i in range(len(Data)):
    if Data[i] in '({':
        stack.append(Data[i])
    elif stack and (Data[i]==')' and stack[-1]=='(') or (Data[i]=='}' and stack[-1]=='{'):
        #닫는 괄호는 스택에 저장되는게 아님
        stack.pop()
    else: break

if not stack : ans = 1

print(ans)