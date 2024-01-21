import sys
sys.stdin = open('input.txt', 'r')
MyMap = [[0 for _ in range(8)] for __ in range(8)]
Visited = [0]*8

V, E = map(int, input().split()) #처음 7,8 불러옴

for i in range(E):
    #그다음 나타나는 길목들 불러옴
    start, stop = map(int, input().split())
    MyMap[start][stop] = 1
    MyMap[stop][start] = 1

def DFS(here):
    print(here)
    Visited[here] = True

    for next in range(V+1): #0~V까지
        if MyMap[here][next] and not Visited[next]:
            DFS(next)
DFS(1)


