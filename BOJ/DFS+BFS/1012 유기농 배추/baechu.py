import sys
sys.stdin = open('input.txt', 'r')

MyMap = []
Queue = []

def isSafe(y,x):
    return 0<=y<M and 0<=x<N and MyMap[y][x] == 1 and not Visited[y][x]

def BFS():
    while Queue:
        cy, cx = Queue.pop(0)

        for dir in range(4):
            newY = cy + dy[dir]
            newX = cx + dx[dir]

            if isSafe(newY, newX):
                Queue.append((newY, newX))
                Visited[newY][newX] = True

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

TC = int(input()) # TC = 2
for i in range(TC):
    M, N, K = map(int,input().split()) # M가로 N세로 K 심어진배추
    Visited = [[False] * N for _ in range(M)]
    MyMap = [[0 for _ in range(N)] for __ in range(M)]
    Wormland = 0
    for j in range(K):
        a, b = map(int,input().split())
        MyMap[a][b] = 1
    for y in range(M):
        for x in range(N):
            if MyMap[y][x] == 1 and not Visited[y][x]:
                startY = y
                startX = x
                Wormland += 1
                Queue = [(startY,startX)]
                Visited[startY][startX] = True
                BFS()

    print(Wormland)
                    # while Queue:
                    #     cy, cx = Queue.pop(0)
                    #     count += 1
                    #
                    #     for dir in range(4):
                    #         newY = cy + dy[dir]
                    #         newX = cx + dx[dir]
                    #
                    #         if isSafe(newY,newX):
                    #             Queue.append([newY,newX])
                    #             Visited[newY][newX] = True





