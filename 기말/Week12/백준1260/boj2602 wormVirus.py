import sys
sys.stdin = open('warmVirus.txt', 'r')

Computer = int(input())
Connected = int(input())

MyMap = [[] for _ in range(Computer+1)]
count = 0

for i in range(Connected):
    start, stop = map(int,input().split())
    MyMap[start].append(stop)
    MyMap[stop].append(start)

    # print(MyMap)

for now in MyMap:
    now.sort()

def DFS(here):
    global count
    Visited[here] = True
    count += 1
    for next in MyMap[here]:
        if not Visited[next]:
            DFS(next)

def BFS(here):
    global count
    Queue = []
    Queue.append(here)
    Visited[here] = True

    while Queue:
        here = Queue.pop(0)
        count += 1
        for next in MyMap[here]:
            if not Visited[next]:
                Queue.append(next)
                Visited[next] = True


Visited = [False] * (Computer + 1)
DFS(1)
print(count - 1)
print()
Visited = [False] * (Computer + 1)
count = 0
BFS(1)
print(count - 1)





