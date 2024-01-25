import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
SeperatedIceAreas = 0
count = 0
MyMap = []
Queue = deque()
yearCount = 0

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

Visited = [[False] * M for _ in range(N)]

for _ in range(N):
    MyMap.append(list(map(int, input().split())))


def isSafe(y, x):
    return 0 <= y < N and 0 <= x < M


def meltIce():
    newMap = [[0] * M for _ in range(N)]

    for y in range(N):
        for x in range(M):
            if MyMap[y][x] > 0:
                melted = 0
                for dir in range(4):
                    newY, newX = y + dy[dir], x + dx[dir]
                    if isSafe(newY, newX) and MyMap[newY][newX] == 0:
                        melted += 1
                newMap[y][x] = max(0, MyMap[y][x] - melted)

    return newMap


while True:
    SeperatedIceAreas = 0
    Visited = [[False] * M for _ in range(N)]

    for y in range(N):
        for x in range(M):
            if MyMap[y][x] > 0 and not Visited[y][x]:
                SeperatedIceAreas += 1
                Queue.append((y, x))
                Visited[y][x] = True

                while Queue:
                    cy, cx = Queue.popleft()

                    for dir in range(4):
                        newY, newX = cy + dy[dir], cx + dx[dir]

                        if isSafe(newY, newX) and MyMap[newY][newX] > 0 and not Visited[newY][newX]:
                            Queue.append((newY, newX))
                            Visited[newY][newX] = True

    if SeperatedIceAreas >= 2:
        print(yearCount)
        break
    elif SeperatedIceAreas == 0:
        print(0)
        break

    MyMap = meltIce()
    yearCount += 1

print(MyMap)





