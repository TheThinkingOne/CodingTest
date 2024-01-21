import sys
sys.stdin = open('input.txt', 'r')

F, S, G, U, D = map(int, input().split())
#총 F층, 스타트링크는 G층, 강호위치 S층, U = Up, D = Down

Queue = []
Time = [987654321]*(F+1)
UpAndDown = [U,-D]
# visited = [False] * (F+1)

def BFS(S):
    Queue.append(S)
    Time[S] = 0
    # visited[S] = True

    while Queue:
        new_S = Queue.pop(0)
        for move in UpAndDown:
            nextFloor = new_S + move

            if 1 <= nextFloor <= F: #and not visited[nextFloor]:
                # visited[nextFloor] = True
                Time[nextFloor] = Time[new_S] + 1
                Queue.append(nextFloor)

    if Time[G] != -1:
        return Time[G]
    else:
        return "Use the Stairs"

result = BFS(S)
print(result)
