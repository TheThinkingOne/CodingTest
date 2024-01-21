import sys
sys.stdin = open('input.txt','r')

N = int(input())
SafeZone = 0
checkingLand = []
height = 1
Visited = [[False]* N for _ in range(N)]


dy = [-1,1,0,0]
dx = [0,0,-1,1]
#Visited = [[False]* N for _ in range(N)]
MyMap = []
Queue = []

def isSafe(y,x):
    return 0<=y<N and 0<=x<N and MyMap[y][x] > N

for __ in range(N):
    MyMap.append(list(map(int, input().split())))

def survivedLand():
    global height
    for row in MyMap:
        while sum(row) != 0:
            height += 1
            if int(MyMap[y][x]) <= 0:

