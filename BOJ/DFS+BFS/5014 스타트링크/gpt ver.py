import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

F, S, G, U, D = map(int, input().split())

def bfs(start, target, max_floor, up, down):
    visited = [False] * (max_floor + 1)
    queue = deque([(start, 0)])  # (현재 층, 이동 횟수)를 담는 큐
    visited[start] = True

    while queue:
        current_floor, moves = queue.popleft()

        if current_floor == target:
            return moves

        up_floor = current_floor + up
        down_floor = current_floor - down

        if up_floor <= max_floor and not visited[up_floor]:
            visited[up_floor] = True
            queue.append((up_floor, moves + 1))

        if down_floor >= 1 and not visited[down_floor]:
            visited[down_floor] = True
            queue.append((down_floor, moves + 1))

    return "Use the Stairs"

result = bfs(S, G, F, U, D)
print(result)
