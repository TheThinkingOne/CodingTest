import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int,input().split())
SeperatedIceAreas = 0
count = 0
MyMap = []
Queue = []
yearCount = 0

dy = [-1,1,0,0]
dx = [0,0,-1,1]

Visited = [[False] * M for _ in range(N)]

for _ in range(N):
    MyMap.append(list(map(int, input().split())))

def isSafe(y,x):
    return 0<=y<N and 0<=x<M

for y in range(N):
    for x in range(M):
        if MyMap[y][x] > 0 and not Visited[y][x]:
            startY = y
            startX = x
            count = 0
            #SeperatedIceAreas += 1
            Queue = [(startY, startX)]
            Visited[startY][startX] = True

            while Queue:
                cy, cx = Queue.pop(0)

                for dir in range(4):
                    newY = cy + dy[dir]
                    newX = cx + dx[dir]

                    if MyMap[newY][newX] == 0:
                        if MyMap[y][x] > 0 and not Visited[newY][newX]:
                            MyMap[y][x] -= 1
                        else:
                            continue
#print(SeperatedIceAreas)
print(MyMap)



# def thawingIceLand(): #
#     global count
#     global yearCount
#     while Queue:
#         cy, cx = Queue.pop(0)
#
#         for dir in range(4):
#             newY = cy + dy[dir]
#             newX = cx + dx[dir]
#
#             if isSafe(newY, newX) and not Visited[newY][newX]:
#                 if MyMap[newY][newX] <= 0:
#                     MyMap[cy][cx] -= 1
#                     if MyMap[cy][cx] < 0:
#                         MyMap[cy][cx] = 0




# def CountingIcebergs():
#     count = 0
#     for y in range(N):
#         for x in range(M):
#             if MyMap[y][x] > 0 and not Visited[y][x]:
#                 Queue = [(y,x)]
#                 Visited[y][x] = True
#                 count += 1
#                 while Queue:
#                     cy, cx = Queue.pop(0)
#                     for dir in range(4):
#                         newY = cy + dy[dir]
#                         newX = cx + dx[dir]
#
#                         if isSafe(newY, newX) and not Visited[newY][newX] and MyMap[newY][newX] > 0:
#                             Queue.append((newY, newX))
#                             Visited[newY][newX] = True
#
#     return count

# if SeperatedIceAreas == 2:
#     print(count)
# else:
#     print(0)

