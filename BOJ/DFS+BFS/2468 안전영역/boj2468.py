import sys
sys.stdin = open('input2.txt', 'r')

N = int(input())
SafeZone = 0
checkingLand = []

dy = [-1,1,0,0]
dx = [0,0,-1,1]
Visited = [[False]* N for _ in range(N)]
MyMap = []
Queue = []

def isSafe(y,x):
    return 0<=y<N and 0<=x<N and int(MyMap[y][x]) > N and not Visited[y][x]

for __ in range(N):
    MyMap.append(input().split())

for y in range(N):
    for x in range(N):
        if int(MyMap[y][x]) <= N:
            checkingLand.append((y,x))
            if len(checkingLand) == 0:
                SafeZone = 1
        else:
            if int(MyMap[y][x]) > N and not Visited[y][x]:
                startY = y
                startX = x
                SafeZone += 1
                Queue = [(startY,startX)]
                Visited[startY][startX] = True

                while Queue:
                    cy, cx = Queue.pop(0)

                    for dir in range(4):
                        newY = cy + dy[dir]
                        newX = cx + dx[dir]

                        if isSafe(newY,newX):
                            Queue.append((newY, newX))
                            Visited[newY][newX] = True

print(SafeZone)

