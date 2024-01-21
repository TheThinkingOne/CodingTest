import sys
sys.stdin = open('input.txt', 'r')

Data = [list(map(int, input().split())) for i in range(5)]

#상하좌우 로직
DeltaY = [-1, 1, 0, 0] #상하
DeltaX = [0, 0, -1, 1] #좌우

def isSafe(y,x): #5x5 범위내에서 작동하게 하는 로직
    if y >= 0 and y <= 4 and x >=0 and x <=4 :
        return True
    else:
        return False

def myAbs(a,b): #절대값
    if a > b:
        return a-b
    else:
        return b-a

sum = 0

for y in range(5):
    for x in range(5):
        for dir in range(4):
            newY = y + DeltaY[dir]
            newX = x + DeltaX[dir]
            if isSafe(newY, newX): #isSafe 범위 내에 있으면 작동
                sum += myAbs(Data[y][x], Data[newY][newX])

print(sum)