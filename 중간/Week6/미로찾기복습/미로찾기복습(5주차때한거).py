import sys
sys.stdin = open('sample_input.txt', 'r')

A = int(input())
def goodToGo(y, x): #1이 아닌곳을 찾아가는 알고리즘
    if 0 <= x < 5 and 0 <= y < 5 and Maze[y][x] != 1:
        return True
    else:
        return False

def DFS(y, x):
    global ans
    if Maze[y][x] == 3:
        ans = 1
        return
    Maze[y][x] = 1
    for dy, dx in (0,1), (0,-1), (-1,0), (1,0): #상하좌우
        newY = y + dy
        newX = x + dx
        if goodToGo(newY, newX):
            DFS(newY, newX)

for tc in range(A):
    B = int(input())
    Maze = [list(map(int, input())) for _ in range(B)]
    ans = 0
    for y in range(B):
        for x in range(B):
            if Maze[y][x] == 2:
                startX = x
                startY = y

    DFS(startY, startX)
    print(f"#{tc} {ans}")


