import sys
sys.stdin = open('input.txt', 'r')

H, W, N, M = map(int, input().split())

MyMap = [[0 for _ in range(W)] for __ in range(H)]
visited = [[False for _ in range(W)] for __ in range(H)]

dy = [-N, N, 0, 0]
dx = [0, 0, -M, M]

def isSafe(y, x):
    return 0 <= y < H and 0 <= x < W and MyMap[y][x] != -1

def bfs(startY, startX):
    Queue = [(startY, startX)]

    while Queue:
        cy, cx = Queue.pop(0)

        for dir in range(4):
            newY = cy + dy[dir]
            newX = cx + dx[dir]

            if isSafe(newY, newX) and not visited[newY][newX]:
                MyMap[newY][newX] += 1
                visited[newY][newX] = True
                Queue.append((newY, newX))

bfs(0, 0)

totalSum = sum(row.count(-1) for row in MyMap)
print(totalSum)



