# import sys
# sys.stdin = open('input.txt','r')
#
# T = int(input())  # T = 3
# def isSafe(y,x):
#     if 0<=y<5 and 0<=x<5 and MyMap[y][x] != 1 and not Visited[y][x]:
#         return True
#     else:
#         return False
#
# for k in range(T):
#     n = int(input()) # n = 5
#     MyMap = [[0 for _ in range(n)] for __ in range(n)]
#     Queue = []
#     dy = [-1,1,0,0]
#     dx = [0,0,-1,1]
#     flag = 0
#     Visited = [[False] * 5 for _ in range(5)]
#
#     for i in range(n): # 마이맵에 미로 한줄씩 추가됨
#         for y in range(n):
#             for x in range(n):
#                 if MyMap[y][x] == 2:
#                     startY = y
#                     startX = x
#                     Queue.append([startY, startX])
#                     Visited[startY][startX] = True
#
#         while Queue:
#             y, x = Queue.pop(0)  # 큐가 현재위치
#             for forward in range(4):
#                 if isSafe(y + dy[forward], x + dx[forward]):
#                     Queue.append([y+dy[forward], x + dx[forward]])
#                     MyMap[y + dy[forward]][x + dx[forward]] = 1
#                 elif MyMap[y + dy[forward]][x+dx[forward]] == 3:
#                     flag = 1
#                     break
#
#         print(f"#{i+1} {flag}")

            # if MyMap[y][x] == 3:
            #     print("Found!")
            # for dir in range(4):
            #     newY = y + dy[dir]
            #     newX = x + dx[dir]
            #     if isSafe(newY, newX):
            #         Visited[newY][newX] = True
            #         Queue.append([newY, newX])

import sys
sys.stdin = open('input.txt', 'r')

T = int(input()) # T = 3

def isSafe(y, x):
    return 0 <= y < N and 0 <= x < N and MyMap[y][x] != 1 and not Visited[y][x]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def solve_maze(startY, startX):
    Queue = ([(startY, startX)])
    Visited[startY][startX] = True

    while Queue:
        y, x = Queue.pop(0)
        if MyMap[y][x] == 3:
            return 1  # 도착지에 도착했음을 나타내는 값

        for forward in range(4):
            ny = y + dy[forward]
            nx = x + dx[forward]
            if isSafe(ny, nx):
                Queue.append((ny, nx))
                Visited[ny][nx] = True

    return 0  # 도착지에 도착하지 못함을 나타내는 값

for k in range(T):
    N = int(input())
    MyMap = []
    for _ in range(N):
        row = list(map(int, input().strip()))
        MyMap.append(row)

    Visited = [[False] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if MyMap[y][x] == 2:
                result = solve_maze(y,x)
                print(f"#{k+1} {result}")











