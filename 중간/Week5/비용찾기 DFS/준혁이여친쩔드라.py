# import sys
# sys.stdin = open('input.txt', 'r') #파일에서 읽을 때
#
# goal, howmany = map(int,input().split())
#
# MyMap = [[0]*(goal+1) for __ in range(goal+1)]
# visited = [0] * (goal+1)
#
# for i in range(howmany):
#     start,end,cost = map(int,input().split())
#     MyMap[start][end] = cost
#     MyMap[end][start] = cost
#
# ans = 0
#
# print(MyMap)

import sys
sys.stdin = open('input.txt', 'r')  # 파일에서 읽을 때

goal, howmany = map(int, input().split())

MyMap = [[0] * (goal + 1) for __ in range(goal + 1)]
visited = [0] * (goal + 1)

for i in range(howmany):
    start, end, cost = map(int, input().split())
    MyMap[start][end] = cost
    MyMap[end][start] = cost

ans = 0

# 각 행별로 요소들의 합을 출력
for row in MyMap:
    row_sum = sum(row)
    min_val = min(row)
    print(row_sum)

