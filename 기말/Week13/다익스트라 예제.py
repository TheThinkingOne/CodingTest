import sys
sys.stdin = open('inputDkstra.txt', 'r')

def getMin(): #최솟값 찾기
    min = INF
    wheremin = -1
    for now in range(V+1): # now = 0~6
        if not Visited[now] and Distance[now] < min:
            min =  Distance[now]
            wheremin = now
    return wheremin

INF = int(1e9)  # 매우 큰숫자
V, E = map(int,input().split()) #V=6, E=13
myMap = [[INF]*(V+1) for __ in range(V+1)] # 7 x 7 마이맵 생성


for __ in range(E):
    start, stop, cost = map(int,input().split())
    myMap[start][stop] = cost
    #ex) myMap[0][1] = 11, myMap[4][2] = 4
Visited = [0] * (V+1)
Distance = [INF] * (V+1)
start = 0
Distance[start] = 0 #시작점에서 시작점 거리 = 0
# print(myMap)
# print(Distance)
for i in range(V+1): # i = 0~6
    # if myMap[i] : Distance[i] = myMap[0][i] # 마이맵 내용을 Distance로 옮김
    Distance[i] = myMap[0][i]

for _ in range(V): # _ = 0~5
    Shortest = getMin()
    Visited[Shortest] = True # 한번 설정된 최솟값을 true 로 설정

    for now in range(V+1): # now가 2일때 Distance[now] = 9
        if Distance[now] > Distance[Shortest] + myMap[Shortest][now]:
            # 9                # 4                  # 3
            Distance[now] = Distance[Shortest] + myMap[Shortest][now]
    print(Distance)

