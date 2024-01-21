# import sys
# sys.stdin = open('input.txt', 'r') #파일에서 읽을 때
#
# def isSafe(y,x):
#     if 0<=x<16 and 0<=y<16 and Maze!=1: #미로의 범위내에 있고 가는지점의 숫자가 1이 아니면 나아감
#         return True
#     else:
#         return False
#
# def DFS(y,x):
#     global ans
#     if Maze[y][x] ==3:
#         ans = 1
#         return
#
#     Maze[y][x] = 1 #도착한위치는 숫자 1로 바꿈
#
#     for dy, dx in (0,1),(0,-1),(-1,0),(1,0): #상하좌우(전에 했던 코드 참고)
#         newY = y + dy
#         newX = x + dx
#         if isSafe(newY,newX):
#             DFS(newY,newX)
#
#
# for tc in range(1,11):
#     T = int(input())
#     Maze = [list(map(int,input())) for _ in range(16)] #한줄씩 총 16줄인 미로 불러오기
#     ans = 0
#
#     for y in range(16):
#         for x in range(16):
#             if Maze[y][x] == 2: #시작점의 숫자가 2라면 시작
#                 startX = x
#                 startY = y
#
#     DFS(startY,startX)
#     print(f"#{tc} {ans}")

import sys
sys.stdin = open('input.txt', 'r') # 파일에서 읽을 때
def isSafe(y, x):
    if  0 <= x < 16 and 0 <= y < 16 and Maze[y][x] != 1 :
    #x,y가 미로 범위 내에 있고 위치의 숫자가 1이 아니면 갈 수 있다
        return True
    else :
        return False
def DFS(y, x):
    #print("x: %d, y:%d"%(x,y))
    global ans
    if Maze[y][x] == 3 :
        ans = 1
        return
    Maze[y][x] = 1
    for dy, dx in (0, 1), (0, -1), (-1, 0), (1, 0):
        newY= y+dy
        newX = x + dx
        if isSafe(newY, newX) :
            DFS(newY, newX)

for tc in range(1, 11):
    T = int(input())
    Maze=[list(map(int,input())) for _ in range(16)]
    ans = 0
    for y in range(16):
        for x in range(16):
            if Maze[y][x] == 2 :
                startX = x
                startY = y
                #return이 있다면? => 인접한 곳이 전부 막혀있을 경우 그자리에서 종료

    DFS(startY, startX)
    print(f"#{tc} {ans}")