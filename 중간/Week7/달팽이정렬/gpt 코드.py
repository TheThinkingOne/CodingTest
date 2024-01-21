import sys

sys.stdin = open('snail.txt', 'r')

n = 5
arr = [list(map(int, input().split())) for _ in range(n)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def is_valid(r, c, n, arr):
    return 0 <= r < n and 0 <= c < n and arr[r][c] == 0

def snail(arr):
    r, c, num = 0, 0, 1
    d = 0
    while num <= n * n:
        arr[r][c] = num
        nr, nc = r + dr[d], c + dc[d]
        if not is_valid(nr, nc, n, arr):
            d = (d + 1) % 4
            nr, nc = r + dr[d], c + dc[d]
        r, c, num = nr, nc, num + 1

snail(arr)

for row in arr:
    print(*row)


