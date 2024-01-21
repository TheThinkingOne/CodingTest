import sys
sys.stdin = open('input.txt', 'r')

H, W, N, M = map(int, input().split())
# H=행, W=열, N=세로, M=가로
MyMap = [[0 for _ in range(H)] for __ in range(W)]
MyMap[0][0] = 1

dy = [-N-1, N+1, 0, 0]
dx = [0, 0, -M-1, M+1]

Visited = [[False for _ in range(H)] for __ in range(W)]

def isSafe(y, x):
    return 0 <= y < W and 0 <= x < H and not Visited[y][x]

startY, startX = 0, 0
Queue = [(startY, startX)]
Visited[startY][startX] = True

while Queue:
    cy, cx = Queue.pop(0)

    for dir in range(4):
        newY = cy + dy[dir]
        newX = cx + dx[dir]

        if isSafe(newY, newX):
            MyMap[newY][newX] += 1
            Queue.append((newY, newX))
            Visited[newY][newX] = True

totalSum = sum(sum(row) for row in MyMap)
print(totalSum)

