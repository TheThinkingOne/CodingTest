import sys
sys.stdin = open('input.txt', 'r')

N = int(input()) # 7x7 크기
AptComplex = 0
ConnectedAptList = []

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
Visited = [[False] * N for _ in range(N)]
MyMap = []
Queue = []

def isSafe(y, x):
    return 0 <= y < N and 0 <= x < N and MyMap[y][x] == '1' and not Visited[y][x]

for __ in range(N):
    MyMap.append(input())

for y in range(N): # 탐색할수 있는지 확인
    for x in range(N):
        if MyMap[y][x] == '1' and not Visited[y][x]:
            startY = y
            startX = x
            count = 0
            AptComplex += 1
            Queue = [(startY, startX)]
            Visited[startY][startX] = True

            while Queue:
                cy, cx = Queue.pop(0)
                count += 1

                for dir in range(4):
                    newY = cy + dy[dir]
                    newX = cx + dx[dir]

                    if isSafe(newY,newX):
                        Queue.append((newY, newX))
                        Visited[newY][newX] = True

            ConnectedAptList.append(count)

ConnectedAptList.sort() #요소 정렬b
print(AptComplex)
for count in ConnectedAptList: #요소 출력
    print(count)

##처음에 내가 짠 코드
# import sys
# sys.stdin = open('input.txt','r')
#
# N = int(input())
# AptComplex = 0
# ConnectedApts = 0
#
# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]
# Visited = [[False] * N for _ in range(N)]
# MyMap = []
# Queue = []
#
# def isSafe(y, x):
#     return 0 <= y < N and 0 <= x < N and MyMap[y][x] == '1' and not Visited[y][x]
#
# for __ in range(N):
#     MyMap.append(input())
#
# for y in range(N): # 탐색할수 있는지 확인
#     for x in range(N):
#         if MyMap[y][x] == 1 and not Visited[y][x]:
#             startY = y
#             startX = x
#             Queue.append([startY][startX])
#             Visited[startY][startX] = True
#             AptComplex += 1
#
# while Queue:
#     y, x = Queue.pop(0)
#     for dir in range(4):
#         newY = y +dy[dir]
#         newX = x +dx[dir]
#
#         while isSafe(newY,newX):
#             Visited[newY][newX] = True
#             Queue.append([newY,newX])
#             ConnectedApts += 1
#         else:
#             Queue = []
#
# print(AptComplex)






