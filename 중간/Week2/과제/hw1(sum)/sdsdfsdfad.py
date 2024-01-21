Data = [
    [1, 2, 3, 4, 5],
    [2, 3, 4, 5, 6],
    [3, 4, 5, 6, 7],
    [4, 5, 6, 7, 8],
    [5, 6, 7, 8, 9]
]

# 각 행의 합을 저장할 리스트
row_sums = []

# 각 행에 대한 합을 계산
for i in range(5):
    row_sum = sum(Data[i])
    row_sums.append(row_sum)
    print(f"행 {i+1}의 합: {row_sum}")

print(row_sums)
print(sum(Data[0]))