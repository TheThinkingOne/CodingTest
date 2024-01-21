import sys
sys.stdin = open('input.txt','r')

N, M, R = map(int,input().split())

MyMap = []
for _ in range(N):
    MyMap.append(list(map(int,input().split())))

print(MyMap)

while True:
    for y in range(N):
        for x in range(M):
            if

