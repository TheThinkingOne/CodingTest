import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
r, c, d = map(int, input().split())
Visited = [[False] * M for _ in range(N)]

MyMap = []
count = 0

for i in range(N):
    MyMap.append(list(map(int, input().split())))

dy = [-1, 0, 1, 0]  # 북, 동, 남, 서 순서
dx = [0, 1, 0, -1]

def isSafe(y, x):
    return 0 <= y < N and 0 <= x < M

def clean(y, x, direction):
    global count

    # 현재 위치 청소
    if MyMap[y][x] == 0:
        count += 1
        MyMap[y][x] = 2  # 청소 표시

    for _ in range(4):  # 4방향 탐색
        direction = (direction + 3) % 4  # 현재 방향 기준 왼쪽 방향부터 탐색
        ny, nx = y + dy[direction], x + dx[direction]

        if isSafe(ny, nx) and MyMap[ny][nx] == 0:  # 청소할 공간이 존재하는 경우
            clean(ny, nx, direction)
            return  # 청소 후 바로 리턴하여 다음 칸으로 이동

    # 네 방향 모두 청소할 곳이 없는 경우 후진
    back_direction = (direction + 2) % 4  # 현재 방향 기준으로 후진 방향 설정
    by, bx = y + dy[back_direction], x + dx[back_direction]
    if isSafe(by, bx) and MyMap[by][bx] != 1:  # 후진할 수 있는 경우
        clean(by, bx, direction)  # 방향은 유지한 채 후진

# 로봇 청소기 시작
clean(r, c, d)
print(count)
