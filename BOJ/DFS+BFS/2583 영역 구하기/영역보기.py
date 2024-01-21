import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

M, N, K = map(int, input().split())
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

Visited = [[False] * M for _ in range(N)]
MyMap = [[0] * M for _ in range(N)]
notColoredLand = []
numOfnotColoredLand = 0

def isSafe(y, x):
    return 0 <= x < M and 0 <= y < N and MyMap[y][x] == 0 and not Visited[y][x]

for _ in range(K):
    y1, x1, y2, x2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            MyMap[y][x] = 1

#print(MyMap)

def BFS(startY, startX):
    count = 0
    Queue = [(startY, startX)]
    Visited[startY][startX] = True

    while Queue:
        cy, cx = Queue.pop(0)
        count += 1

        for dir in range(4):
            newY = cy + dy[dir]
            newX = cx + dx[dir]

            if isSafe(newY, newX):
                Queue.append((newY, newX))
                Visited[newY][newX] = True

    notColoredLand.append(count)

for y in range(N):
    for x in range(M):
        if MyMap[y][x] == 0 and not Visited[y][x]:
            BFS(y, x)
            numOfnotColoredLand += 1

notColoredLand.sort()
print(numOfnotColoredLand)
for land in notColoredLand:
    print(land, end=' ')

