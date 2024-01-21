Data = [2,3,5,4,1,6,7,8,10,12]

for i in range(len(Data)): #단계
    for j in range(len(Data)-1): #거품의 이동 횟수(거품은 단계마다 길이의 -1 만큼 시행되므로)
        if Data[j] > Data[j+1]:
            Data[j], Data[j+1] = Data[j+1], Data[j] #버블정렬 비교한거 순서 바꾸기

print(Data)