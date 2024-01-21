import sys
sys.stdin = open('input.txt', 'r')
Data = [list(map(int, input().split())) for i in range(5)]

max = sum = 0

#전치행렬 만들기
for y in range(5):
    for x in range(5):
        if y > x:
            Data[y][x], Data[x][y] = Data[x][y], Data[y][x]
print(Data)

#가로 합의 최대값 구하기
for y in range(5):
    for x in range(5):
        sum+=Data[y][x]
    if sum > max: max = sum
    print(sum)
    sum = 0








