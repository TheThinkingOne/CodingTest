import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(T):
    Data = list(map(int, input().split()))
    maxVal_index = Data.index(max(Data))
    minVal_index = Data.index(min(Data))
    #print(maxVal_index)
    #첫번째 줄의 경우 max(Data) = 87, Data.index(max(Data)) = 6
    #그러므로 Data[maxVal_index] = 6
    Data[maxVal_index], Data[minVal_index] = Data[minVal_index], Data[maxVal_index]
    print(f"#{tc + 1}", " ".join(map(str, Data)))





