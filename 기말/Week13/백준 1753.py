import sys
sys.stdin = open('1753input.txt')
def getMin(StartPoint):
    min_distance = INF
    wheremin = -1
    Visited[StartPoint] = 1  # 시작점 방문 표시
    for now in range(1, V + 1):
        if not Visited[now] and Distance[now] < min_distance:
            min_distance = Distance[now]
            wheremin = now
    return wheremin

INF = 99
V, E = map(int, input().split())
StartPoint = int(input())
MyMap = [[INF] * (V + 1) for _ in range(V + 1)]

for _ in range(E):
    start, stop, cost = map(int, input().split())
    MyMap[start][stop] = cost

Visited = [0] * (V + 1)
Distance = [INF] * (V + 1)
Distance[StartPoint] = 0

for i in range(1, V + 1):
    if MyMap[StartPoint][i] != INF:
        Distance[i] = MyMap[StartPoint][i]

for _ in range(V):
    Shortest = getMin(StartPoint)
    if Shortest == -1:  # 더 이상 갈 수 있는 노드가 없을 때
        break
    Visited[Shortest] = True

    for now in range(1, V + 1):
        if not Visited[now] and Distance[now] > Distance[Shortest] + MyMap[Shortest][now]:
            Distance[now] = Distance[Shortest] + MyMap[Shortest][now]

for i in range(1, V + 1):
    if Visited[i]:
        print(Distance[i])
    else:
        print("INF")





