# import sys
# sys.stdin = open('input.txt', 'r')
#
# N, K = map(int, input().split())
#
# Queue = []
# ability = [1, -1, 2]
#
# visited = [-1] * 100001
# visited[N] = 0
# # count = 0
# def BFS(here):
#     Queue.append(here)
#     while Queue:
#         here = Queue.pop(0)
#         # count += 1
#         for i in ability:
#             if i == 2:
#                 next = here*2
#             else:
#                 next = here + i
#
#             if 0 <= next <= 300003 and visited[next] == -1:
#                 visited[next] = visited[here] + 1
#                 Queue.append(next)
#
#                 if next == K:
#                     return visited[next]
#
# result = BFS(N)
# print(result)
# if Time[E]!=987654321:print(Time[E]) # 경로에 간 곳에 있으면
# else : print(-1) # 길이 연산을 통해 갔는데도 도달을 못 한다면

# from collections import deque
#
# V, E = 5, 17  # 주어진 값으로 설정
#
# Queue = deque()
# ability = [1, -1, 2]
# visited = [-1] * 100001  # 방문한 적이 없는 경우 -1로 표시
# visited[V] = 0  # 시작점은 0으로 설정
#
# def BFS(start):
#     Queue.append(start)
#
#     while Queue:
#         here = Queue.popleft()
#
#         for move in ability:
#             if move == 2:
#                 next_pos = here * 2
#             else:
#                 next_pos = here + move
#
#             if 0 <= next_pos <= 100000 and visited[next_pos] == -1:
#                 visited[next_pos] = visited[here] + 1
#                 Queue.append(next_pos)
#
#                 if next_pos == E:  # 목표 지점에 도달했을 때
#                     return visited[next_pos]
#
# result = BFS(V)
# print(result)  # 5에서 17까지의 최단 시간 출력

import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

N, K = map(int, sys.stdin.readline().split())

Queue = []
ability = [1, -1, 2]

visited = [-1] * 300003
visited[N] = 0

# time = [987654321]*(300003)
# time[N] = 0

def BFS(here):
    while Queue:
        here = Queue.pop(0)
        for i in ability:
            if i == 2:
                next = here * 2
            else:
                next = here + i

            if 0 <= next < 100000 and visited[next] == -1:
                visited[next] = visited[here] + 1
                Queue.append(next)
                if next == K:
                    return visited[next]
            elif next < 0:
                # 음수로 이동하는 경우를 처리하거나 건너뛰도록 설정합니다.
                continue

Queue.append(N)
result = BFS(N)
print(result)
