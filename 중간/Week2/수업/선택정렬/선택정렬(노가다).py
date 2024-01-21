#p.34~ 참고
Data = [3,2,5,4,1]

def getMin(start,end):
    min = Data[start]
    wheremin = start

    for i in range(start, end+1):
        if Data[i] < min:
            min = Data[i]
            wheremin = i

    return wheremin

for here in range(len(Data)-1):
    where = getMin(here, 4)
    Data[here], Data[where] = Data[where], Data[here]

print(Data)