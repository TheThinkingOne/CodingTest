Data = [3,2,5,4,1,6]
howmany = len(Data)

def getSome(now):
    if now == howmany-1: return
    where = Data.index(min(Data[now:howmany]))
    Data[now], Data[where] = Data[where], Data[now]
    getSome(now+1)

getSome(0)
print(Data)
#Data 정렬순서
#now=0일때 => [1,2,5,4,3,6]