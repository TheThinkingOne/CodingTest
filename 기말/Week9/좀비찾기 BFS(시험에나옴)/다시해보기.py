# import sys
# sys.stdin = open('input.txt', 'r') # 파일에서 읽을 때 사용
#
# Time = [987654321] * 1000
# ability = [0]*3
# Queue = []
# def BFS(here):
#     while Queue:
#         here = Queue.pop(0)
#         for i in range(3):
#             next = here + ability[i] # + 2, 5, 7
#             if next < 0 or next > len(Time) - 1 : continue
#             if Time[next] > Time[here] + 1:
#                 Time[next] = Time[here] + 1
#                 Queue.append(next)
#
# for i in range(4):
#     Slayer, Zombie = map(int,input().split())
#     ability[0], ability[1], ability[2] = map(int,input().split())
#     Time[Slayer] = 0
#     if Slayer == Zombie:
#         Queue.append(Slayer)
#         BFS(Slayer)
#     else:
#         Queue.append(Slayer)
#         BFS(Slayer)
#
#     if Time[Zombie]!= 987654321 : print(Time[Zombie])
#     else : print(-1)

import sys

sys.stdin = open('input.txt', 'r')

Time = [987654321] * 1000
ability = [0] * 3
Queue = []


def BFS(here):
    while Queue:
        here = Queue.pop(0)
        for i in range(3):
            next = here + ability[i]  # + 2, 5, 7
            if next < 0 or next > len(Time) - 1:
                continue
            if Time[next] > Time[here] + 1:
                Time[next] = Time[here] + 1
                Queue.append(next)


for _ in range(4):
    Slayer, Zombie = map(int, input().split())
    ability[0], ability[1], ability[2] = map(int, input().split())

    Time[Slayer] = 0
    Queue.append(Slayer)
    BFS(Slayer)

    if Time[Zombie] != 987654321:
        print(Time[Zombie])
    else:
        print(-1)








