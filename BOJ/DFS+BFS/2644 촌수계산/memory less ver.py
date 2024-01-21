import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

Queue = deque()
n = int(input())
kindred1, kindred2 = map(int, input().split())
m = int(input())

MyMap = [[0 for _ in range(n+1)] for __ in range(n+1)]
Distance = [0]*(n+1)
Parent = [-1]*(n+1)
Visited = [False] *(n+1)

for i in range(m):
    parent, child = map(int, input().split())
    MyMap[parent][child] = 1
    MyMap[child][parent] = 1

def BFS(kindred):
    Queue.append(kindred)
    Visited[kindred] = True

    while Queue:
        here = Queue.popleft()

        for next in range(1, n+1):
            if MyMap[here][next] and not Visited[next] and next not in Queue:
                Queue.append(next)
                Visited[next] = True
                Distance[next] = Distance[here] + 1
                Parent[next] = here
                if next == kindred2:
                    return Distance[next]
                break

    return -1

result = BFS(kindred1)
if result > 0:
    print(result)
else:
    print(-1)
