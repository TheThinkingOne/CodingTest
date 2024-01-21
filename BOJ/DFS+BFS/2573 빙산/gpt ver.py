import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
SeperatedIceAreas = 0
MyMap = []
Queue = []
yearCount = 0

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

Visited = [[False] * M for _ in range(N)]

for _ in range(N):
    MyMap.append(list(map(int, input().split())))  # Split 후 int 변환하여 2차원 배열 생성

# 함수 정의
def isSafe(y, x):
    return 0 <= y < N and 0 <= x < M

def IceLand():
    while Queue:
        cy, cx = Queue.pop(0)
        for dir in range(4):
            newY = cy + dy[dir]
            newX = cx + dx[dir]

            if isSafe(newY, newX) and not Visited[newY][newX]:
                if MyMap[newY][newX] <= 0:
                    MyMap[cy][cx] -= 1
                    if MyMap[cy][cx] < 0:
                        MyMap[cy][cx] = 0

def countIcebergs():
    count = 0
    for y in range(N):
        for x in range(M):
            if MyMap[y][x] > 0 and not Visited[y][x]:
                Queue = [(y, x)]
                Visited[y][x] = True
                count += 1
                while Queue:
                    cy, cx = Queue.pop(0)
                    for dir in range(4):
                        newY = cy + dy[dir]
                        newX = cx + dx[dir]

                        if isSafe(newY, newX) and not Visited[newY][newX] and MyMap[newY][newX] > 0:
                            Queue.append((newY, newX))
                            Visited[newY][newX] = True

    return count

# 빙산 녹는 과정과 분리되는 시점 확인
while True:
    SeperatedIceAreas = countIcebergs()

    if SeperatedIceAreas == 0:
        print(0)
        break

    if SeperatedIceAreas >= 2:
        print(yearCount)
        break

    yearCount += 1
    for y in range(N):
        for x in range(M):
            if MyMap[y][x] > 0:
                for dir in range(4):
                    newY = y + dy[dir]
                    newX = x + dx[dir]

                    if isSafe(newY, newX) and MyMap[newY][newX] <= 0:
                        MyMap[y][x] -= 1
                        if MyMap[y][x] < 0:
                            MyMap[y][x] = 0

    Visited = [[False] * M for _ in range(N)]

# 코드 종료
