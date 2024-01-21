import sys #p.20 문제
sys.stdin = open('input.txt', 'r')

Data = [list(map(int, input().split())) for i in range(9)]

max = Data[0][0]
whereY, whereX = -1, -1

for y in range(9): #열부터 순회
    for x in range(9): #그다음 행 순회
        if Data[y][x] > max:
            max = Data[y][x]
            whereY = y
            whereX = x

print(max)
print(whereY+1, whereX+1)