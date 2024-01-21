import sys
sys.stdin = open('input.txt', 'r')

V, E, Start = map(int,input().split())

MyMap = [[] for _ in range(V+1)]

for __ in range(E):
    __from, __to = map(int,input().split()) # __from = 1, __to = 2
    MyMap[__from].append(__to)
    MyMap[__to].append(__from)

for now in MyMap:
    now.sort()

def DFS(here):
    print(here, end='')
    Visited[here] = True
    for next in MyMap[here]:
        if not Visited[next]:
            DFS(next)

def BFS(here):
    Q = []
    Q.append(here)
    Visited[here] = True

    while Q:
        here = Q.pop(0)
        print(here, end='')
        for next in MyMap[here]:
            if not Visited[next]:
                Q.append(next)
                Visited[next] = True

Visited = [False] * (V+1)
DFS(Start)
print()
Visited = [False] * (V+1)
BFS(Start)