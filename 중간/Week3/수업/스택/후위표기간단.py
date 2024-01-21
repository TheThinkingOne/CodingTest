Data = "2+3&4/5"
Data2 = "6+5*(2-8)/2"

stack = []
Result = []

for i in range(len(Data2)):
    if'*'<=Data2[i]<='/':
        stack.append(Data2[i])
    elif '0'<=Data2[i]<='9':
        Result.append(Data2[i])

while stack:
    Result.append(stack.pop())
print(''.join(Result))