import sys
sys.stdin = open('input.txt', 'r')

M, N = map(int,input().split()) # M=6, N=4
MyMap = []
Queue = []
count = 0
emptyBoxList = 0

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for _ in range(N):
    lines = sys.stdin.readline().split()
    MyMap.append([int(x) for x in lines])



Visited = [[False] * M for _ in range(N)]

def isSafe(y,x):
    return 0<=y<N and 0<=x<M and MyMap[y][x] == 0

def BFS():
    global count
    while Queue:
        cy, cx = Queue.pop(0)

        for dir in range(4):
            newY = cy + dy[dir]
            newX = cx + dx[dir]

            if isSafe(newY, newX) and MyMap[newY][newX] == 0:
                Queue.append((newY, newX))
                MyMap[newY][newX] = 1
        #         Visited[newY][newX] = True
        #
        # count += 1



# for y in range(N):
#     for x in range(M):
#         if MyMap[y][x] == -1:
#             emptyBoxList += 1
#         if MyMap[y][x] == 1 and not Visited[y][x]:
#             Queue.append((y,x))
#             Visited[y][x] = True
#             BFS()
#             #-1인 곳을 제외한 0이 모두 1이 되면 count 출력
#             # if sum(MyMap) - emptyBoxList == N*M - emptyBoxList:
#             #     print(count)
#             # else:
#             #     print(-1)
# if sum(row.count() for row in MyMap) == emptyBoxList:
#     print(count)
# else:
#     print(-1)
for y in range(N):
    for x in range(M):
        if MyMap[y][x] == -1:
            emptyBoxList += 1
        if MyMap[y][x] == 1 and not Visited[y][x]:
            Queue.append((y,x))
            Visited[y][x] = True
            BFS()

# 모든 0이 1로 변했다면 count 출력, 아니면 -1 출력
if sum(row.count(0) for row in MyMap) == emptyBoxList:
    print(count)
else:
    print(-1)


