Data = [3,2,5,4,1,6]
howmany = len(Data)

def getSome(now):
    if now==howmany-1: return
    where = Data.index(min(Data[now:howmany]))
    Data[now], Data[where] = Data[where], Data[now] #위치 바꿈
    getSome(now+1)

getSome(0)
print(Data)