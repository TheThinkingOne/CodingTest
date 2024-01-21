
#
# import sys
#
# sys.stdin = open('input.txt', 'r')
#
# def dfs(graph, start):
#     visited = [False] * (V + 1)
#     stack = [start]
#
#     while stack:
#         here = stack.pop()
#         if not visited[here]:
#             visited[here] = True
#             print(here)
#
#             for neighbor in range(1, V + 1):
#                 if graph[here][neighbor] and not visited[neighbor]:
#                     stack.append(neighbor)
#
# V, E = map(int, input().split())
# MyMap = [[0 for _ in range(V + 1)] for _ in range(V + 1)]
#
# for _ in range(E):
#     start, stop = map(int, input().split())
#     MyMap[start][stop] = 1
#     MyMap[stop][start] = 1
#
# dfs(MyMap, 1)

import sys

sys.stdin = open('input.txt', 'r')

V, E = map(int, input().split())
adj_list = [[] for _ in range(V+1)] # V=0~7, 8개의 빈 리스트 생성

for _ in range(E): # 0~7
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

def dfs(graph, start):
    visited = [False] * (V + 1)
    stack = [start]

    while stack:
        here = stack.pop()
        if not visited[here]:
            visited[here] = True
            print(here)

            for neighbor in reversed(graph[here]):
                if not visited[neighbor]:
                    stack.append(neighbor)

dfs(adj_list, 1)



