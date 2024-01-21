import sys
sys.stdin = open('inputASC.txt', 'r')

stack=[]
Info = [0] * 128 #아스키코드는 7비트라 ['('] = ')', ['('] = '}' , ['('] = ']' , ['('] = '>'

Info[ord(')')] = '('
Info[ord('}')] = '{'
Info[ord(']')] = '['
Info[ord('>')] = '<'

Data = input()

for i in range(len(Data)):
    if Data[i] in '{[(<':
        stack.append(Data[i])
    elif stack[-1] == Info[ord(Data[i])]:
        stack.pop()

print(Info)
