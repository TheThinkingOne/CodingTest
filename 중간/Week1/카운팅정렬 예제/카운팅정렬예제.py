import sys

sys.stdin = open('input.txt', 'r') # 파일에서 읽을 때 사용

Data = list(map(int, input().split()))

howmany = len(Data)

Count = [0] * 5 #길이가 5인 리스트 선언
Result = [0] * howmany #변수의 크기가 howmany인 리스트 선언

for i in range(howmany): #i는 데이터의 길이 까지
    Count[Data[i]] += 1

for i in range(1, len(Count)):
    Count[i] += Count[i-1]

for i in range(len(Data) - 1, -1, -1):
    Count[Data[i]]-=1
    Result[Count[Data[i]]] = Data[i]

print(Result)