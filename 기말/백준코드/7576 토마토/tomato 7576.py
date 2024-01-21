import sys
sys.stdin = open('input.txt','r')

M, N = map(int,input().split()) # M=6, N=4
MyMap = []
Queue = []

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

Visited = [[False] * N for _ in range(M)]

def isSafe(y,x):
    return 0<=y<M and 0<=x<N and MyMap[y][x] != '-1' and not Visited[y][x]

def BFS():
    global count
    count = 0
    while Queue:
        cy, cx = Queue.pop(0)

        for dir in range(4):
            newY = cy + dy[dir]
            newX = cx + dx[dir]

            if isSafe(newY, newX):
                Queue.append((newY, newX))
                MyMap[newY][newX] = '1'
                Visited[newY][newX] = True
                count += 1

for _ in range(M):
    lines = map(int,input().split())
    MyMap.append(lines)

for y in range(M):
    for x in range(N):
        count = 0
        if MyMap[y][x] == '1' and not Visited[y][x]:
            Queue.append((y,x))
            Visited[y][x] = True
            BFS()
            all_ones = all('1' in row for row in MyMap)
            if all_ones:
                print(count)
            else:
                print(-1)


