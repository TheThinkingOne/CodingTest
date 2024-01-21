import sys
sys.stdin = open('input.txt','r')
from collections import deque

N, M = map(int, sys.stdin.readline().split())

numOfPainting = 0
paintingSizeList = []

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

Visited = [[False] * M for _ in range(N)]
MyMap = []
Queue = deque()  # deque 활용

def isSafe(y, x):
    return 0 <= y < N and 0 <= x < M and MyMap[y][x] == '1'

MyMap = [sys.stdin.readline().split() for _ in range(N)]  # sys.stdin.readline() 직접 사용

for y in range(N):
    for x in range(M):
        if MyMap[y][x] == '1' and not Visited[y][x]:
            startY = y
            startX = x
            count = 0
            numOfPainting += 1
            Queue.append((startY, startX))
            Visited[startY][startX] = True

            while Queue:
                cy, cx = Queue.popleft()  # deque에서 popleft() 사용
                count += 1

                for dir in range(4):
                    newY = cy + dy[dir]
                    newX = cx + dx[dir]

                    if isSafe(newY, newX) and not Visited[newY][newX]:
                        Queue.append((newY, newX))
                        Visited[newY][newX] = True

            paintingSizeList.append(count)

# 결과 출력
print(numOfPainting)
if paintingSizeList:  # 그림이 하나도 없는 경우 0 출력
    print(max(paintingSizeList))
else:
    print(0)