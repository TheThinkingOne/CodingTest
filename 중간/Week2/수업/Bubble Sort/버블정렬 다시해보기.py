Data = [2,3,5,4,1,6,7,8,10,12]

for i in range(len(Data)):
    for j in range(len(Data)-1):
        if Data[j] > Data[j+1]:
            Data[j], Data[j+1] = Data[j+1], Data[j]

    print(Data)