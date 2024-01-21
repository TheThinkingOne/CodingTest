from collections import deque
import sys
sys.stdin = open('input.txt', 'r')
# 입력값 받기
M, N, H = map(int, input().split())
MyMap = []

for _ in range(H):
    temp = []
    for __ in range(N):
        temp.append(list(map(int, input().split())))
    MyMap.append(temp)
    #(x,y,z)의 꼴로 좌표를 나타낼 수 있음

#print(MyMap)

# 상하좌우 탐색
dy = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def isSafe(z, y, x):
    return 0 <= z < H and 0 <= y < N and 0 <= x < M

def BFS():
    days = -1  # 처음에 1부터 시작하므로 -1로 초기화
    Queue = deque()

    # 익은 토마토의 위치를 큐에 넣음
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if MyMap[i][j][k] == 1:
                    Queue.append((i, j, k))

    while Queue:
        size = len(Queue) #출발 1이 여러개므로
        for _ in range(size):
            z, y, x = Queue.popleft()

            for dir in range(6):
                newZ = z + dz[dir]
                newY = y + dy[dir]
                newX = x + dx[dir]

                if isSafe(newZ, newY, newX) and MyMap[newZ][newY][newX] == 0:
                    MyMap[newZ][newY][newX] = 1
                    Queue.append((newZ, newY, newX))

        days += 1

    return days

# 최소 일수 계산
result = BFS()

# 결과 출력
for i in range(H):
    for row in MyMap[i]:
        if 0 in row:
            result = -1  # 익지 않은 토마토가 남아있다면


print(result)  # 모든 토마토가 익었다면 최소 일수 출력