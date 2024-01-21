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
    global flag, Distance, minDistance
    while Queue:
        y, x, d = Queue.pop(0)
        for dir in range(4):
            newY = y + dy[dir]
            newX = x + dx[dir]
            if isSafe(newY, newX):
                Visited[newY][newX] = True
                Queue.append((newY, newX, d + 1))
                if MyMap[newY][newX] == 3:  # 도착점인 3을 찾았을 때
                    flag = 1
                    Distance = d  # 거리는 d가 됨
                    minDistance = min(minDistance, d)  # 최소 거리 갱신
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
    minDistance = float('inf')  # 최소 거리를 저장할 변수, 초기값은 무한대로 설정
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
    if minDistance == float('inf'):
        minDistance = 0
    print(f"#{i + 1} {minDistance}")
