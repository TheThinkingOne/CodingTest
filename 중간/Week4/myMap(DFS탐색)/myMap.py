import sys
sys.stdin = open('input.txt', 'r')
MyMap = [[0 for _ in range(8)] for __ in range(8)]
Visited = [0]*8 #갔는지 안갔는지 표시하는 것

V, E = map(int, input().split())

for _ in range(E):
    start, stop = map(int, input().split())
    MyMap[start][stop] = 1
    MyMap[stop][start] = 1

def DFS(here):
    print(here)
    Visited[here] = True

    for next in range(V+1):
        if MyMap[here][next] and not Visited[next]:
            #파이썬은 정의되지 않은 부분은 무시하고 다음 값으로 넘김
            DFS(next)
DFS(1)
