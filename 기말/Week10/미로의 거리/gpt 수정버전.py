# import sys
# sys.stdin = open('input.txt','r')
#
# T = int(input()) # T = 3
# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]
#
# def isSafe(y,x):
#     if 0<=y<N and 0<=x<N and MyMap[y][x] != 1 and not Visited[y][x]:
#         return True
#     else:
#         return False
#
# def BFS():
#     global flag, Distance
#     while Queue:
#         y, x = Queue.pop(0)
#         for dir in range(4):
#             newY = y + dy[dir]
#             newX = x + dx[dir]  # 수정된 부분: x + dx[dir]로 변경
#             if isSafe(newY, newX):
#                 Visited[newY][newX] = True
#                 Queue.append([newY, newX])
#                 Timeline[newY][newX] = Timeline[y][x] + 1
#                 MyMap[newY][newX] = 1
#             elif MyMap[newY][newX] == 3:
#                 flag = 1
#                 Distance = Timeline[y][x]
#                 return
#
# for i in range(T):
#     N = int(input())
#     MyMap = []
#     Timeline = []
#     for _ in range(N):
#         row = list(map(int, input().strip()))
#         MyMap.append(row)
#     for k in range(N):
#         Timeline.append([0] * N)  # 수정된 부분: N+2에서 N으로 변경
#     Visited = [[False] * N for _ in range(N)]
#     Queue = []
#     Distance = 0
#     flag = 0
#     for y in range(N):
#         for x in range(N):
#             if MyMap[y][x] == 2:
#                 Visited[y][x] = True
#                 Queue.append([y, x])
#                 BFS()
#     print(f"#{i+1} {Distance}")

# import sys
# sys.stdin = open('input.txt', 'r')
#
# T = int(input())  # T = 3
# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]
#
# def isSafe(y, x):
#     if 0 <= y < N and 0 <= x < N and MyMap[y][x] != 1 and not Visited[y][x]:
#         return True
#     else:
#         return False
#
# def BFS():
#     global flag, Distance
#     while Queue:
#         y, x, d = Queue.pop(0)
#         for dir in range(4):
#             newY = y + dy[dir]
#             newX = x + dx[dir]  # 수정된 부분: x + dx[dir]로 변경
#             if isSafe(newY, newX):
#                 Visited[newY][newX] = True
#                 Queue.append((newY, newX, d + 1))
#                 MyMap[newY][newX] = 1
#                 if MyMap[newY][newX] == 3:
#                     flag = 1
#                     Distance = d + 1
#                     return
#
# for i in range(T):
#     N = int(input())
#     MyMap = []
#     for _ in range(N):
#         row = list(map(int, input().strip()))
#         MyMap.append(row)
#     Visited = [[False] * N for _ in range(N)]
#     Queue = []
#     Distance = 0
#     flag = 0
#     for y in range(N):
#         for x in range(N):
#             if MyMap[y][x] == 2:
#                 Visited[y][x] = True
#                 Queue.append((y, x, 0))
#                 BFS()
#                 if flag == 1:
#                     break
#         if flag == 1:
#             break
#     print(f"#{i+1} {Distance}")

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())  # T = 3
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def isSafe(y, x):
    if 0 <= y < N and 0 <= x < N and MyMap[y][x] != 1 and not Visited[y][x]:
        return True
    else:
        return False

def BFS():
    global flag, Distance
    while Queue:
        y, x, d = Queue.pop(0)
        for dir in range(4):
            newY = y + dy[dir]
            newX = x + dx[dir]
            if isSafe(newY, newX):
                Visited[newY][newX] = True
                Queue.append((newY, newX, d + 1))
                # MyMap[newY][newX] = 1 이 부분 지움
                if MyMap[newY][newX] == 3:  # 도착점인 3을 찾았을 때
                    flag = 1
                    Distance = d  # 거리는 d + 1이 됨
                    return

for i in range(T):
    N = int(input())
    MyMap = []
    for _ in range(N):
        row = list(map(int, input().strip()))
        MyMap.append(row)
    Visited = [[False] * N for _ in range(N)]
    Queue = []
    Distance = 0
    flag = 0
    for y in range(N):
        for x in range(N):
            if MyMap[y][x] == 2:
                Visited[y][x] = True
                Queue.append((y, x, 0))
                BFS()
                if flag == 1:
                    break
        if flag == 1:
            break
    print(f"#{i+1} {Distance}")





