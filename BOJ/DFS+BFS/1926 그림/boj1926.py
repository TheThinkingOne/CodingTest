import sys
sys.stdin = open('input.txt','r')
sys.setrecursionlimit(10**7)

N, M = map(int, sys.stdin.readline().split())

numOfPainting = 0
paintingSizeList = []

dy = [-1,1,0,0]
dx = [0,0,-1,1]

Visited = [[False] * M for _ in range(N)]
MyMap = []
Queue = []

def isSafe(y,x):
    return 0<=y<N and 0<=x<M and MyMap[y][x] == 1

for _ in range(N):
    MyMap.append(list(map(int,input().split())))

for y in range(N):
    for x in range(M):
        if MyMap[y][x] == 1 and not Visited[y][x]:
            startY = y
            startX = x
            count = 0
            numOfPainting += 1
            Queue = [(startY,startX)]
            Visited[startY][startX] = True

            while Queue:
                cy, cx = Queue.pop(0)
                count += 1

                for dir in range(4):
                    newY = cy + dy[dir]
                    newX = cx + dx[dir]

                    if isSafe(newY,newX) and not Visited[newY][newX]:
                        Queue.append((newY,newX))
                        Visited[newY][newX] = True

            paintingSizeList.append(count)


print(numOfPainting)
print(max(paintingSizeList))

