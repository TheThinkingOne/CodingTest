# import sys
# sys.stdin = open('input.txt','r')
#
# N, M = map(int, input().split())
# MyMap = []
# Queue = []
#
# dy = [-1,1,0,0]
# dx = [0,0,-1,1]
#
# Visited = [[False] * M for __ in range(N)]
#
# # def isSafe(y,x):
# #     if 0<=y<N and 0<=y<M and MyMap[y][x] != '0' and not Visited[y][x]:
# #         return True
# #     else:
# #         return False
# def isSafe(y, x):
#     return 0 <= y < N and 0 <= x < M and MyMap[y][x] == '1' and not Visited[y][x]
#
# for __ in range(N):
#     MyMap.append(list(input().strip()))
#
# Queue.append((0,0))
# Visited[0][0] = True
#
# while Queue:
#     y, x = Queue.pop(0)
#     # if y == N-1 and x == M-1:
#     for dir in range(4):
#         newY = y + dy[dir]
#         newX = x + dy[dir]
#         if isSafe(newY,newX):
#             Visited[newY][newX] = True
#             Queue.append((newY,newX))
#             MyMap[newY][newX] = int(MyMap[y][x]) + 1
#             if newY == N -1 and newX == M-1:
#                 Queue = []
#
# print(MyMap[N-1][M-1])

import sys
sys.stdin = open('input.txt','r')

N, M = map(int, input().split()) # N:세로(y), M:가로(x)
MyMap = []
Queue = []

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

Visited = [[False] * M for _ in range(N)]


def isSafe(y, x):
    return 0 <= y < N and 0 <= x < M and MyMap[y][x] == '1' and not Visited[y][x]


for _ in range(N):
    MyMap.append(list(input()))  # 각 줄을 리스트로 받음

Queue.append((0, 0))
Visited[0][0] = True

while Queue:
    y, x = Queue.pop(0)

    for dir in range(4):
        newY = y + dy[dir]
        newX = x + dx[dir]

        if isSafe(newY, newX):
            Visited[newY][newX] = True
            Queue.append((newY, newX))
            MyMap[newY][newX] = int(MyMap[y][x]) + 1  # 이동 횟수를 1 증가시킴
            if newY == N - 1 and newX == M - 1:  # 도착점에 도달했을 때 더 이상 탐색하지 않고 종료
                Queue = []

print(MyMap[N - 1][M - 1])

