import sys
sys.stdin = open('input.txt', 'r')
MyMap = [[0 for _ in range(8)] for __ in range(8)]
Visited = [0] * 8#갔는지 안갔는지 표시하는 것
Queue = []

Distance = [0]*8
Parent = [-1]*8

V, E = map(int, input().split())

for _ in range(E):
    start, stop = map(int, input().split())
    MyMap[start][stop] = 1
    MyMap[stop][start] = 1

start = 1
Queue.append(start) #큐에 원소 1 저장
Distance[start] = 0 # Distance[1] = 0
Parent[start] = 0 # Parent[1] = 0

while Queue: #큐가 비어있지 않은 경우
    here = Queue.pop(0) #현위치
    print(here)
    Visited[here] = True #방문위치 체크

    for next in range(8):
        if MyMap[here][next] and not Visited[next] and next not in Queue:
            #길이 있고 방문한적이 없고 next가 다음 큐에 없다면
            Queue.append(next)
            Distance[next] = Distance[here] + 1
            Parent[next] = here #부모가 이전의 next 가 되는것

    print(Distance)