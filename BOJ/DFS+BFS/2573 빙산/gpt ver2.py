import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
MyMap = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def isSafe(y, x):
    return 0 <= y < N and 0 <= x < M

def meltIce():
    new_map = [row[:] for row in MyMap]  # 녹은 빙산을 새로운 맵으로 복사
    for y in range(N):
        for x in range(M):
            if MyMap[y][x] > 0:
                sea_count = sum(1 for ny, nx in zip([y-1, y+1, y, y], [x, x, x-1, x+1]) if isSafe(ny, nx) and MyMap[ny][nx] == 0)
                new_map[y][x] = max(0, MyMap[y][x] - sea_count)

    return new_map

def countIcebergs():
    count = 0
    visited = [[False] * M for _ in range(N)]
    for y in range(N):
        for x in range(M):
            if MyMap[y][x] > 0 and not visited[y][x]:
                count += 1
                stack = [(y, x)]
                visited[y][x] = True

                while stack:
                    cy, cx = stack.pop()
                    for dir in range(4):
                        ny, nx = cy + dy[dir], cx + dx[dir]
                        if isSafe(ny, nx) and MyMap[ny][nx] > 0 and not visited[ny][nx]:
                            stack.append((ny, nx))
                            visited[ny][nx] = True

    return count

yearCount = 0
while True:
    icebergCount = countIcebergs()

    if icebergCount == 0:
        print(0)
        break

    if icebergCount >= 2:
        print(yearCount)
        break

    MyMap = meltIce()
    yearCount += 1
