import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')

N, M = map(int,input().split())
r, c, d = map(int,input().split())
Visited = [[False] * N for _ in range(M)]

MyMap = []
count = 0

for i in range(N):
    MyMap.append(input().split())

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def isSafe(y,x):
    return 0 <= y < N and 0 <= x < M

def ifSumIs4(y, x, dircetion):
    if dircetion == 0:
        if isSafe(y+1,x):
            Queue.append((y + 1, x, dircetion))
    elif dircetion == 1:
        if isSafe(y,x-1):
            Queue.append((y + 1, x, dircetion))
    elif dircetion == 2:
        if isSafe(y-1,x):
            Queue.append((y + 1, x, dircetion))
    elif dircetion == 3:
        if isSafe(y,x+1):
            Queue.append((y + 1, x, dircetion))

def ifSumIsNot4(y, x, direction):
    if direction == 0:
        direction = 3 #북->서
        if isSafe(y, x-1) and MyMap[y][x-1] != 1:
            Queue.append((y, x - 1, direction))
        else:
            ifSumIsNot4(y, x - 1, direction)
    elif direction == 1:
        direction = 0 #동->북
        if isSafe(y-1, x) and MyMap[y-1][x] != 1:
            Queue.append((y - 1, x, direction))
        else:
            ifSumIsNot4(y - 1, x, direction)
    elif direction == 2:
        direction = 1 #남->동
        if isSafe(y, x+1) and MyMap[y][x+1] != 1:
            Queue.append((y, x + 1, direction))
        else:
            ifSumIsNot4(y, x + 1, direction)
    elif direction == 3:
        direction = 2 #서->남
        if isSafe(y+1, x) and MyMap[y+1][x] != 1:
            Queue.append((y + 1, x, direction))
        else:
            ifSumIsNot4(y + 1, x, direction)

startY = r
startX = c
direction = d
Queue = [(startY, startX, direction)]

while Queue:
    cy, cx, new_d = Queue.pop(0)
    if MyMap[cy][cx] == 0:
        count += 1
        MyMap[cy][cx] = 2

    for dir in range(4):
        newY = cy + dy[dir]
        newX = cx + dx[dir]

        if newY + newX == 4:
            ifSumIs4(cy, cx, direction)
        elif newY + newX != 4:
            ifSumIsNot4(cy, cx, direction)

print(count)





