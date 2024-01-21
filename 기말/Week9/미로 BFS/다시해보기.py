import sys
sys.stdin = open('input.txt', 'r') # 파일에서 읽을 때 사용

row, col = map(int,input().split())
MyMap=[]
Queue=[]
dy = [-1,1,0,0]
dx = [0,0,-1,1]
Visited = [[0] * col for _ in range(row)]

def isSafe(y,x):
    if 0<=y<5 and 0<=x<5 and MyMap[y][x] != '#' and not Visited[y][x]:
        return True
    else:
        return False

for __ in range(row):
    MyMap.append(input())

for y in range(5):
    for x in range(5):
        if MyMap[y][x] == 'S':
            startY = y
            startX = x
            Queue.append([startY, startX])
            Visited[startY][startX] = True

while Queue:
    y, x = Queue.pop(0)
    if MyMap[y][x] == 'G':
        print("End")
    for dir in range(4):
        newY = y +dy[dir]
        newX = x +dx[dir]
        if isSafe(newY,newX):
            Visited[newY][newX] = True
            Queue.append([newY,newX])


