import sys
sys.stdin = open('input5x5.txt', 'r') # 파일에서 읽을 때
def isSafe(y,x):
    if 0<= x < 5 and 0<= y < 5 and Maze[y][x] !=1:
        return True
    else:
        return False
def DFS(y,x):
    global ans
    if Maze[y][x] == 3:
        ans = 1
        return
    Maze[y][x] = 1
    for dy, dx in (0, 1), (0, -1), (-1, 0), (1, 0):
        newY = y + dy
        newX = x + dx
        if isSafe(newY, newX):
            DFS(newY, newX)

Maze=[list(map(int,input())) for _ in range(5)]
ans = 0
for y in range(5):
    for x in range(5):
        if Maze[y][x] == 2 :
            startX = x
            startY = y

DFS(startY, startX)
print(f"# {ans}")