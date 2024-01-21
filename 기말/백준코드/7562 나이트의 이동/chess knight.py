import sys
sys.stdin = open('input.txt','r')

dy = [2,2,1,1,-1,-1,-2,-2]
dx = [1,-1,2,-2,2,-2,1,-1]

def isSafe(y,x):
    return 0<=y<length and 0<=x<length and not Visited[y][x]

def BFS(y,x):
    while Queue:
        y, x, moves = Queue.pop(0)
        if y == goal1 and x == goal2:
            return moves
        for dir in range(8):
            newY = y + dy[dir]
            newX = x + dx[dir]

            if isSafe(newY, newX):
                Visited[newY][newX]= True
                Queue.append((newY,newX,moves+1))
                    # if MyMap[newY][newX] == MyMap[goal1][goal2]:
                    #     count += 1
                    #     print(count)
                    # else:
                    #     Visited[newY][newX] = True
                    #     Queue.append((newY, newX))
                    #     count += 1

TC = int(input())
for i in range(TC):
    Queue = []
    length = int(input())
    start1, start2 = map(int,input().split())
    goal1, goal2 = map(int,input().split())
    # MyMap = [[0 for _ in range(length)] for __ in range(length)]
    Visited = [[False] * length for _ in range(length)]

    if start1 == goal1 and start2 == goal2:
        print(0)
    else:
        Queue.append((start1,start2,0))
        Visited[start1][start2] = True
        result = BFS(start1,start2)
        print(result)

# import sys
# sys.stdin = open('input.txt', 'r')
#
# dy = [2, 2, 1, 1, -1, -1, -2, -2]
# dx = [1, -1, 2, -2, 2, -2, 1, -1]
#
# def isSafe(y, x):
#     return 0 <= y < length and 0 <= x < length and not Visited[y][x]
#
# def BFS(y, x):
#     while Queue:
#         y, x, moves = Queue.pop(0)  # 이동 횟수를 함께 저장
#         if y == goal1 and x == goal2:
#             return moves  # 목표 지점에 도착했을 때 이동 횟수 반환
#         for dir in range(8):
#             newY = y + dy[dir]
#             newX = x + dx[dir]
#
#             if isSafe(newY, newX):
#                 Visited[newY][newX] = True
#                 Queue.append((newY, newX, moves + 1))
#
# TC = int(input())
# for _ in range(TC):
#     Queue = []
#     length = int(input())
#     start1, start2 = map(int, input().split())
#     goal1, goal2 = map(int, input().split())
#     Visited = [[False] * length for _ in range(length)]
#
#     if start1 == goal1 and start2 == goal2:
#         print(0)  # 시작점과 끝점이 동일한 경우 0 출력
#     else:
#         Queue.append((start1, start2, 0))
#         Visited[start1][start2] = True
#         result = BFS(start1, start2)
#         print(result)








