import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

N, K = map(int, sys.stdin.readline().split())

Queue = deque()
ability = [1, -1, 2]

visited = [-1] * 300003
visited[N] = 0

def BFS(start):
    Queue.append(start)
    while Queue:
        here = Queue.popleft()
        for i in ability:
            if i == 2:
                next = here * 2
            else:
                next = here + i

            if 0 <= next < 300003 and visited[next] == -1:
                visited[next] = visited[here] + 1
                Queue.append(next)
                if next == K:
                    return visited[next]
            elif next < 0:
                continue

result = BFS(N)
print(result)
