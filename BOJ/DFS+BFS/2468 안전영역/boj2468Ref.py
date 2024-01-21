import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
SafeZone = 0
checkingLand = []
height = 0

dy = [-1,1,0,0]
dx = [0,0,-1,1]
Visited = [[False]* N for _ in range(N)]
MyMap = []
Queue = []

def isSafe(y,x):
    return 0<=y<N and 0<=x<N and not Visited[y][x]

for __ in range(N):
    MyMap.append(input().split())
    for i in range(len(MyMap)):
        MyMap[i] = list(map(int, MyMap[i]))

def newMap():
    global height
    while height < 100:
        # for y in range(N):
        #     for x in range(N):
        #         MyMap[y][x] -= height
        #         if int(MyMap[y][x]) < 0:
        #             MyMap[y][x] = 0
        #             for row in MyMap:
        #                 if int(row) < 0:
        #                     break
        for row in MyMap:
            if all(row) <= height:
                break
            else:
                height += 1
        return MyMap, height

for y in range(N):
    for x in range(N):
        if int(MyMap[y][x]) > height:
            #MyMap[y][x] = int(MyMap[y][x]) - N
            checkingLand.append((y,x))
            if len(checkingLand) == 0:
                SafeZone = 1
        else:
            if MyMap[y][x] > height and not Visited[y][x]:
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

