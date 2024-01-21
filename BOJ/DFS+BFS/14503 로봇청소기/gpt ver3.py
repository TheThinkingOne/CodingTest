import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
r, c, d = map(int, input().split()) # x,y 좌표와 현재 바라보는 방향

MyMap = []
count = 0

for i in range(N):
    MyMap.append(list(map(int, input().split())))

dy = [-1, 0, 1, 0]  # 북,남
dx = [0, 1, 0, -1]  # 동,서

def isSafe(y, x):
    return 0 <= y < N and 0 <= x < M

def cleaning(): #BFS
    global count
    stack = [(r, c, d)]  # 청소할 위치와 방향을 저장하는 스택

    while stack:
        y, x, direction = stack.pop()
        if MyMap[y][x] == 0:
            count += 1
            MyMap[y][x] = 2  # 청소 표시

        # 현재 방향을 기준으로 왼쪽 방향부터 차례대로 탐색
        for _ in range(4):
            direction = (direction + 3) % 4 # 나머지 = 새 방향
            ny, nx = y + dy[direction], x + dx[direction] # 새 전진 좌표

            if isSafe(ny, nx) and MyMap[ny][nx] == 0:
                stack.append((ny, nx, direction))  # 청소할 위치와 방향을 스택에 추가
                break
        else:  # 4방향 모두 청소할 곳이 없는 경우 후진
            back_direction = (direction + 2) % 4 # 바라보는 방향 그대로 후진
            by, bx = y + dy[back_direction], x + dx[back_direction]

            if isSafe(by, bx) and MyMap[by][bx] != 1:
                stack.append((by, bx, direction))  # 후진할 위치와 방향을 스택에 추가

# 로봇 청소기 시작
cleaning()
print(count)
