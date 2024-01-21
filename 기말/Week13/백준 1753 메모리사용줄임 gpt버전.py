import sys
import heapq

INF = int(1e9)

def dijkstra(start):
    distance = [INF] * (V + 1)
    distance[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        dist, now = heapq.heappop(heap)
        if distance[now] < dist:
            continue

        for nxt, cost in graph[now]:
            new_cost = dist + cost
            if new_cost < distance[nxt]:
                distance[nxt] = new_cost
                heapq.heappush(heap, (new_cost, nxt))

    return distance

V, E = map(int, sys.stdin.readline().split())
start_point = int(sys.stdin.readline())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    start, stop, cost = map(int, sys.stdin.readline().split())
    graph[start].append((stop, cost))

result = dijkstra(start_point)

for i in range(1, V + 1):
    if result[i] == INF:
        print("INF")
    else:
        print(result[i])


