import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt','r')

N, M = map(int,sys.stdin.readline().split()) #N=6,M=5
count = 0
MyMap = [[0 for _ in range(N+1)] for __ in range(N+1)]
Visited = [False] * (N+1)

for i in range(M):
    start, stop = map(int,sys.stdin.readline().split())
    MyMap[start][stop] = 1
    MyMap[stop][start] = 1

def DFS(here):
    Visited[here] = True
    for next in range(1, N+1):
        if MyMap[here][next] and not Visited[next]:
            DFS(next)

for i in range(1, N+1):
    if not Visited[i]:
        count += 1
        DFS(i)

print(count)

