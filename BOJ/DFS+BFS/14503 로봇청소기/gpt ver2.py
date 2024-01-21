import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int,input().split())
r, c, d = map(int,input().split())

MyMap = []
count = 0

for i in range(N):
    MyMap.append(list(map(int, input().split())))

dy = [-1, 0, 1, 0]  # 북, 동, 남, 서
dx = [0, 1, 0, -1]

def isSafe(y, x):
    return 0 <= y < N and 0 <= x < M

def ifSumIs4(y, x, direction):
    if direction == 0:
        if isSafe(y+1, x):
            Queue.append((y + 1, x, direction))
    elif direction == 1:
        if isSafe(y, x-1):
            Queue.append((y, x - 1, direction))
    elif direction == 2:
        if isSafe(y-1, x):
            Queue.append((y - 1, x, direction))
    elif direction == 3:
        if isSafe(y, x+1):
            Queue.append((y, x + 1, direction))

def ifSumIsNot4(y, x, direction):
    if direction == 0:
        direction = 3  # 북쪽일 경우 왼쪽으로 방향 변경
        if isSafe(y, x-1) and MyMap[y][x-1] == 0:
            Queue.append((y, x - 1, direction))
        else:
            ifSumIsNot4(y, x - 1, direction)
    elif direction == 1:
        direction = 0  # 동쪽일 경우 위쪽으로 방향 변경
        if isSafe(y-1, x) and MyMap[y-1][x] == 0:
            Queue.append((y - 1, x, direction))
        else:
            ifSumIsNot4(y - 1, x, direction)
    elif direction == 2:
        direction = 1  # 남쪽일 경우 오른쪽으로 방향 변경
        if isSafe(y, x+1) and MyMap[y][x+1] == 0:
            Queue.append((y, x + 1, direction))
        else:
            ifSumIsNot4(y, x + 1, direction)
    elif direction == 3:
        direction = 2  # 서쪽일 경우 아래쪽으로 방향 변경
        if isSafe(y+1, x) and MyMap[y+1][x] == 0:
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

