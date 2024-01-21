import sys #p.20 문제
sys.stdin = open('input.txt', 'r')

Data = [list(map(int,input().split())) for _ in range(9)]
maxVal = Data[0][0]
whereY, whereX = -1, -1

for y in range(len(Data)):
    for x in range(len(Data)):
        if Data[y][x] > maxVal :
            maxVal = Data[y][x]
            whereY = y
            whereX = x

print(maxVal)
print(whereY)
print(whereX)


