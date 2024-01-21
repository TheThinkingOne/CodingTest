import sys
sys.stdin = open('input2.txt', 'r')
from collections import deque

N = int(input())
my_map = []
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for _ in range(N):
    my_map.append(list(map(int, input().split())))

def BFS(height):
    visited = [[False] * N for _ in range(N)]
    count = 0

    for i in range(N):
        for j in range(N):
            if my_map[i][j] > height and not visited[i][j]:
                count += 1
                visited[i][j] = True
                q = deque([(i, j)])

                while q:
                    y, x = q.popleft()
                    for dir in range(4):
                        newY, newX = y + dy[dir], x + dx[dir]
                        if 0 <= newY < N and 0 <= newX < N and my_map[newY][newX] > height and not visited[newY][newX]:
                            visited[newY][newX] = True
                            q.append((newY, newX))

    return count

max_safe_zone = 1
for h in range(1, 101):  # 높이 1부터 100까지 탐색
    max_safe_zone = max(max_safe_zone, BFS(h))

print(max_safe_zone)




