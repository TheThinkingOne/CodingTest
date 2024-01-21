import sys
sys.stdin = open('input.txt', 'r')
def isSafe(y, x):
    if  0 <= x < N and 0 <= y < N and (maze[y][x] ==0 or maze[y][x] ==3) : return True
    else : return False

def DFSr(y, x):
 global found, footprint
 #if not 0 <= x < N or not 0 <= y < N or found or maze[x][y] == 1 : return
 if maze[y][x] == 3 : found = 1; return
 footprint += 1
 maze[y][x] = footprint
 for dy, dx in (0, 1), (0, -1), (-1, 0), (1, 0):
     newY = y + dy
     newX = x + dx
     if isSafe(newY, newX):
         DFSr(newY, newX)


T = int(input())
for tc in range(1, T + 1):
 N = int(input())
 maze = [[int(x) for x in input()] for _ in range(N)]

 for i in range(N):
     for j in range(N):
         if maze[i][j] == 2 :
             sX = i
             sY = j

 footprint = 100
 found = 0
 DFSr(sX, sY)
 for i in range(N):
    print(maze[i])
 print('#%d'%tc, found)