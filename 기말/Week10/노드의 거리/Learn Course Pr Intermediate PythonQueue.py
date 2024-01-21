# V=노드개수, E=간선의 수
# S=시작점, G=목표지점
# import sys
# sys.stdin = open('input.txt','r')
#
# def BFS(here):
#     while Queue:
#         here = Queue.pop(0)
#         for next in range(V+1):
#             if MyMap[here][next] == 1:
#                 if Distance[next] > Distance[here] + 1:
#                     Distance[next] = Distance[here] + 1
#                     Queue.append(next)
#
# TC = int(input())
# for i in range(1, TC+1):
#     V, E = map(int, input().split())
#     MyMap = [[0 for _ in range(V+1)] for __ in range(V+1)]
#     for j in range(E):
#         start, stop = map(int, input().split())
#         MyMap[start][stop] = 1
#         MyMap[stop][start] = 1
#     S, G = map(int, input().split())
#     Distance = [987654321] * 50
#     Queue = [S]
#
#     Distance[S] = 0
#     if S == G:
#         print(0)
#     else:
#         BFS(S)
#     print(f'#{i} {Distance[G]}')


# V=노드개수, E=간선의 수
# S=시작점, G=목표지점
# import sys
# sys.stdin = open('input.txt','r')
#
# def BFS(here):
#     while Queue:
#         here = Queue.pop(0) #처음에 스타지점이 팝됨
#         for next in range(V+1):
#             if MyMap[here][next] == 1:
#                 if Distance[next] > Distance[here] + 1:
#                     Distance[next] = Distance[here] + 1
#                     Queue.append(next)
#
# TC = int(input())
# for i in range(1, TC+1):
#     V, E = map(int, input().split())
#     MyMap = [[0 for _ in range(V+1)] for __ in range(V+1)]
#     for j in range(E):
#         start, stop = map(int, input().split())
#         MyMap[start][stop] = 1
#         MyMap[stop][start] = 1
#     Start, Finish = map(int, input().split())
#     Distance = [987654321]*50
#     Queue = [Start] #큐에 시작점 추가
#
#     Distance[Start] = 0
#     if Start == Finish:
#         print(0)
#     else:
#         BFS(Start)
#     print(f"#{i} {Distance[Finish]}")

import sys
sys.stdin = open('input.txt', 'r')

def BFS(here):
    while Queue:
        here = Queue.pop(0) #처음에 스타지점이 팝됨
        for next in range(V+1):
            if MyMap[here][next] == 1:
                if Distance[next] > Distance[here] + 1:
                    Distance[next] = Distance[here] + 1
                    Queue.append(next)

TC = int(input())
for i in range(1, TC+1):
    V, E = map(int, input().split())
    MyMap = [[0 for _ in range(V+1)] for __ in range(V+1)]
    for j in range(E):
        start, stop = map(int, input().split())
        MyMap[start][stop] = 1
        MyMap[stop][start] = 1
    Start, Finish = map(int, input().split())
    Distance = [987654321]*50
    Queue = [Start] #큐에 시작점 추가

    Distance[Start] = 0
    BFS(Start)

    if Distance[Finish] <= 987654321:
        print(f"#{i} {Distance[Finish]}")
    else:
        print(f"#{i} -1")








