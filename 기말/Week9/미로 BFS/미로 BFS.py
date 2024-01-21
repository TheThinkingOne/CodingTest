# import sys
# sys.stdin = open('input.txt', 'r') # 파일에서 읽을 때 사용
#
# row, col = map(int, input().split()) # row, col = 5
# MyMap=[]
# Queue=[]
# Visited=[[0] * col for _ in range(row)]
# def isPossible(y, x):
#     if 0<=y<5 and 0<=x <5 and MyMap[y][x] != '#' and not Visited[y][x]:
#         return True
#     else :
#         return False
#
# dy = [-1,1,0,0]
# dx = [0,0,-1,1]
# for _ in range(row):
#     MyMap.append(input())
#
# for y in range(5):
#     for x in range(5):
#         if MyMap[y][x] == 'S' :
#             startY = y
#             startX = x
#             Queue.append([startY, startX])
#             Visited[startY][startX] = True
# while Queue:
#     y, x = Queue.pop(0)
#     if MyMap[y][x] == 'G' :
#         print(" 끗 ")
#     for dir in range(4):
#         newY=y+dy[dir]
#         newX = x + dx[dir]
#         if isPossible(newY, newX):
#             Visited[newY][newX] = True
#             Queue.append([newY, newX])

import sys
sys.stdin = open('input.txt', 'r') # 파일에서 읽을 때 사용

row, col = map(int, input().split()) #row, col = 5
MyMap=[]
Queue=[]
Visited=[[0] * col for _ in range(row)]
def isPossible(y, x):
    if 0<=y<5 and 0<=x<5 and MyMap[y][x] != '#' and not Visited[y][x]:
        return True
    else :
        return False

dy = [-1,1,0,0]
dx = [0,0,-1,1]
for _ in range(row): #row = 5
    MyMap.append(input()) #마이맵에 미로 한줄씩 추가됨
    #MyMap = ['#S###', '#...#', '#.#.#', '#....', '###G#']

for y in range(5):
    for x in range(5):
        if MyMap[y][x] == 'S':
            startY = y
            startX = x
            Queue.append([startY, startX]) #큐에 시작점 추가
            Visited[startY][startX] = True

while Queue:
    y, x = Queue.pop(0)
    if MyMap[y][x] == 'G' :
        print(" 끗 ")
    for dir in range(4):
        newY = y+dy[dir] #위의 dx,dy참조
        newX = x + dx[dir]
        if isPossible(newY, newX):
            Visited[newY][newX] = True
            Queue.append([newY, newX]) #큐에 새로운 시작점 추가

