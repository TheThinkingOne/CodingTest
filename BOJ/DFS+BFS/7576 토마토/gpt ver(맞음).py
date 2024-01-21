from collections import deque
import sys
sys.stdin = open('input.txt', 'r')
# 입력값 받기
M, N = map(int, input().split())
MyMap = []
for _ in range(N):
    MyMap.append(list(map(int, input().split())))

# 상하좌우 탐색
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def isSafe(y, x):
    return 0 <= y < N and 0 <= x < M

def BFS():
    days = -1  # 처음에 1부터 시작하므로 -1로 초기화
    Queue = deque()

    # 익은 토마토의 위치를 큐에 넣음
    for i in range(N):
        for j in range(M):
            if MyMap[i][j] == 1:
                Queue.append((i, j))

    while Queue:
        size = len(Queue) #출발 1이 여러개므로
        for _ in range(size):
            y, x = Queue.popleft()

            for dir in range(4):
                newY = y + dy[dir]
                newX = x + dx[dir]

                if isSafe(newY, newX) and MyMap[newY][newX] == 0:
                    MyMap[newY][newX] = 1
                    Queue.append((newY, newX))

        days += 1

    return days

# 최소 일수 계산
result = BFS()

# 결과 출력
for row in MyMap:
    if 0 in row:
        print(-1)  # 익지 않은 토마토가 남아있다면
        break
else:
    print(result)  # 모든 토마토가 익었다면 최소 일수 출력









