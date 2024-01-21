import sys
sys.stdin = open('input.txt', 'r')

F, S, G, U, D = map(int, input().split())
#총 F층, 스타트링크는 G층, 강호위치 S층, U = Up, D = Down

Queue = []
Time = [987654321]*(F+1)
UpAndDown = [U,-D]
visited = [False] * (F+1)
visited[S] = True
Time[S] = 0

def BFS(S):
    while Queue:
        new_S = Queue.pop(0)

        # 여기서 Time[S]랑 visited[S] 를 수정해줘야함
        for i in UpAndDown:
            nextFloor = new_S + i
            if 1 <= nextFloor <= F and not visited[nextFloor]:
                visited[nextFloor] = True
                Time[nextFloor] = Time[new_S] + 1
                Queue.append(nextFloor)

    if visited[G] == True and Time[G] != 987654321:
        return Time[G]
    else:
        return "Use the Stairs"

Queue.append(S)
result = BFS(S)
print(result)