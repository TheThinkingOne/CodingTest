import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for i in range(t):
    n = int(input())
    for j in range(n+2):
        x, y = map(int,input().split())
        MyMap = [[0 for _ in range(max(x,y))] for __ in range(max(x,y))]
        Visited = [0] * max(x,y)
        Queue = []

        start = 0
        Queue.append(start)

        while Queue:
            here = Queue.pop(0)

            for next in range(max(x,y)):
