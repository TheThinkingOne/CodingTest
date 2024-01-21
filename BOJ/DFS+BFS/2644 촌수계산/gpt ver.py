import sys
sys.stdin = open('input.txt', 'r')

Queue = []
n = int(input())
kindred1, kindred2 = map(int, input().split())
m = int(input())

MyMap = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
Visited = [False] * (n + 1)
Distance = [0] * (n + 1)
Parent = [-1] * (n + 1)

for i in range(m):
    parent, child = map(int, input().split())
    MyMap[parent][child] = 1
    MyMap[child][parent] = 1

def BFS(kindred):
    Queue.append(kindred)
    Visited[kindred] = True

    while Queue:
        here = Queue.pop(0)

        for next_node in range(1, n + 1):
            if MyMap[here][next_node] and not Visited[next_node]:
                Queue.append(next_node)
                Visited[next_node] = True
                Distance[next_node] = Distance[here] + 1
                Parent[next_node] = here
                if next_node == kindred2:
                    return Distance[next_node]
                break

    return False

result = BFS(kindred1)
if result > 0:
    print(result)
else:
    print(-1)

