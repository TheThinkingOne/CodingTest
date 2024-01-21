import sys
sys.stdin = open('input5x5.txt', 'r')

Data = [list(map(int, input().split())) for i in range(5)]

row_sums = []
col_sums = []
dig_sums = []

# 행들의 각 합 구하기
# y,x 를 이용한 2중 for문 사용한게 아닌 하나만 이용
for y in range(len(Data)):
    colSum = sum(Data[y])
    #Data는 list형으로 묶었으므로 행별의 합으로 구하는 것과 똑같다.
    col_sums.append(colSum)

# 열들의 각 합 구하기
for x in range(len(Data[0])):
    rowSum = sum(Data[y][x] for y in range(5))
    #Data[0][0], Data[1][0], ... , Data[4][0]
    #Data[0][1], Data[1][1], ... , Data[4][1]
    row_sums.append(rowSum)

# 주 대각선의 합
diagSum1 = sum(Data[i][i] for i in range(len(Data)))
dig_sums.append(diagSum1)

# 부 대각선의 합
diagSum2 = sum(Data[i][len(Data)-1-i] for i in range(len(Data)))
dig_sums.append(diagSum2)

maxVal = max(max(row_sums), max(col_sums), max(dig_sums))

print(max(row_sums))
print(max(col_sums))
print(max(dig_sums))

print(maxVal)

