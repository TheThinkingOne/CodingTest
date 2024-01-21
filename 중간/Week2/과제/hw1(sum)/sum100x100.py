import sys

sys.stdin = open('input100x100.txt', 'r')
T = 10  # 10개의 테스트 케이스

for test_case in range(1, T + 1):
    tempTC = int(input())  # 테스트 케이스 번호를 읽어옵니다.

    Data = [list(map(int, input().split())) for tempTC in range(100)]

    row_sums = []
    col_sums = []
    dig_sums = []

    # 행들의 합
    for y in range(len(Data)):
        rowSum = sum(Data[y])
        row_sums.append(rowSum)

    # 열들의 합
    for x in range(len(Data[0])): #len(Data[0]) = 100
        colSum = sum(Data[y][x] for y in range(100))
        #[0][0],[1][0],[2],[0],...~ [98][99], [99][99]순서
        col_sums.append(colSum)

    # 주 대각선의 합
    diagSum1 = sum(Data[i][i] for i in range(len(Data)))
    dig_sums.append(diagSum1)

    # 부 대각선의 합
    diagSum2 = sum(Data[i][len(Data) - 1 - i] for i in range(len(Data)))
    dig_sums.append(diagSum2)

    maxVal = max(max(row_sums), max(col_sums), max(dig_sums))

    print(f"#{test_case} {maxVal}")
