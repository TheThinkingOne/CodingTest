import sys
sys.stdin = open('input.txt', 'r')

H, W, N, M = map(int,input().split())
#H=행, W=열, N=세로, M=가로
MyMap = [[0 for _ in range(H)] for __ in range(W)]
MyMap[0][0] = 1
print(MyMap)

dy = [-N-1,N+1,0,0]
dx = [0,0,-M-1,M+1]

Visited = [[False for _ in range(H)] for __ in range(W)]
#Visited[0][0] = True

def isSafe(y,x):
    return 0<=y<W and 0<=x<H and not Visited[y][x]

y, x = 0,0
Visited[y][x] = True

for dir in range(4):
    while True:  # 해당 방향으로 무한히 진행
        new_y = y + dy[dir]
        new_x = x + dx[dir]

        if not isSafe(new_y, new_x):
            break  # 배열을 벗어나면 while문 종료

        MyMap[new_y][new_x] += 1
        Visited[new_y][new_x] = True

        y, x = new_y, new_x  # 현재 좌표 업데이트

print(MyMap)







