import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
SeperatedIceAreas = 0
count = 0
MyMap = []
Stack = []  # Change from Queue to Stack for DFS
yearCount = 0

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

Visited = [[False] * M for _ in range(N)]

for _ in range(N):
    MyMap.append(list(map(int, input().split())))

def isSafe(y, x):
    return 0 <= y < N and 0 <= x < M

def dfs(y, x):
    Stack.append((y, x))
    Visited[y][x] = True

    while Stack:
        cy, cx = Stack.pop()

        for dir in range(4):
            newY = cy + dy[dir]
            newX = cx + dx[dir]

            if isSafe(newY, newX) and not Visited[newY][newX]:
                if MyMap[newY][newX] == 0:
                    if MyMap[y][x] > 0:
                        MyMap[y][x] -= 1
                else:
                    dfs(newY, newX)

for y in range(N):
    for x in range(M):
        if MyMap[y][x] > 0 and not Visited[y][x]:
            SeperatedIceAreas += 1
            dfs(y, x)

#print(SeperatedIceAreas)
print(MyMap)


