# import sys
# sys.stdin = open('input.txt','r')
#
# N, M, V = map(int,input().split())
# MyMap = [[0 for _ in range(M)] for __ in range(M)]
# Visited = [0]*(N+1)
# Queue = []
#
# for ___ in range(M):
#     start, stop = map(int,input().split())
#     MyMap[start][stop] = 1
#     MyMap[stop][start] = 1
#
# def DFS(here):
#     print(here, end=' ')
#     Visited[here] = True
#
#     for next in range(N+1):
#         if MyMap[here][next] and not Visited[next]:
#             DFS(next)
#
# def BFS(here):
#     Queue.append(here)
#     Visited[here] = True
#
#     while Queue:
#         current = Queue.pop(0)
#         print(current, end=' ')
#
#         for next in range(1, N + 1):
#             if MyMap[current][next] and not Visited[next]:
#                 Queue.append(next)
#                 Visited[next] = True
#     #     Visited[here] = True
#     #
#     #     for next in range(N+1): #첫 케이스에서 next = 0,1,2,3,4
#     #         if MyMap[here][next] and not Visited[next] and next not in Queue:
#     #             Queue.append(next)
# Visited = [0] * (N+1)
# DFS(V)
# print()
#
# Visited = [0] * (N+1)
# Queue = []
# BFS(V)
import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

N, M, V = map(int, input().split())
MyMap = [[] for _ in range(N + 1)]

for _ in range(M):
    start, stop = map(int, input().split())
    MyMap[start].append(stop)
    MyMap[stop].append(start)

print(MyMap)

for edges in MyMap:
    edges.sort()

def DFS(here):
    Visited[here] = True
    print(here, end=' ')

    for next in MyMap[here]:
        if not Visited[next]:
            DFS(next)

def BFS(start):
    Queue = deque([start])
    Visited[start] = True

    while Queue:
        current = Queue.popleft()
        print(current, end=' ')

        for next in MyMap[current]:
            if not Visited[next]:
                Queue.append(next)
                Visited[next] = True

Visited = [False] * (N + 1)
DFS(V)
print()

Visited = [False] * (N + 1)
BFS(V)


