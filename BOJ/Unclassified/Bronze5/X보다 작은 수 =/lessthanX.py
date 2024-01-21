import sys
sys.stdin = open('input.txt', 'r')

N, X = map(int, input().split())
Data = list(map(int, input().split()))
Warehouse = []

for i in range(N):
    if Data[i] < X:
        Warehouse.append(Data[i])
result = ' '.join(map(str, Warehouse))
print(result)


