import sys
sys.stdin = open('input.txt', 'r')

T = int(input()) # T=3
dy = [-1, 1, 0, 0]
dx = [0, 0 , -1 ,1]

def BFS():
    global flag, Distance
    while Queue:
        y, x = Queue.pop(0)
        for i in range(4):
            if MyMap[y+dy[i]][x+dx[i]] == 0:
                Queue.append([y+dy[i], x+dx[i]])
                Timeline[y+dy[i]][x+dx[i]] = Timeline[y][x] + 1 # 거리 저장
                MyMap[y][x] = 1
            elif MyMap[y+dy[i]][x+dx[i]] == 3:
                flag =1
                Distance = Timeline[y][x]
                return


for j in range(T):
    flag = 0
    Distance = 0
    size = int(input()) # size = 미로의 크기
    MyMap = [[1]*(size+2)]
    Timeline = []
    for k in range(size+2): # k = 0,1,2,3,4,5,6
        Timeline.append([0]*(size+2))

    Queue = []

    for l in range(size): #l = 0,1,2,3,4
        line = list(map(int, input()))
        line.insert(0,1)
        line.append(1)
        MyMap.append(line)
        if 2 in line:
            startY, startX = l+1, line.index(2)
    MyMap.append([1]*(size+2))

    Queue.append([startY, startX])
    BFS()

    print(f"#{j+1} {Distance}")