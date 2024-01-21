import sys
sys.stdin = open('input5x5.txt', 'r')

Data = [list(map(int, input().split())) for _ in range(5)]

# 행, 열, 대각선 합 저장할 배열 정의 (각각의 총합들)
colSums = []
rowSums = []
digSums = []

# 각 행과 열의 합 계산 및 저장
for y in range(len(Data)):
    rowSum = sum(Data[y])
    rowSums.append(rowSum)

for x in range(len(Data)):
    colSum = sum(Data[y][x] for y in range(len(Data)))
    colSums.append(colSum)

# 주 대각선의 합 계산 및 저장
for i in range(len(Data)):
    digSum = Data[i][i]
    digSums.append(digSum)

# 세 합 중에서 가장 큰 값을 찾음
maxColSum = max(colSums)
maxRowSum = max(rowSums)
maxDigSum = max(digSums)
maxSum = max(maxColSum, maxRowSum, maxDigSum)

print(maxColSum)
print(maxRowSum)
print(maxDigSum)
print(maxSum)
