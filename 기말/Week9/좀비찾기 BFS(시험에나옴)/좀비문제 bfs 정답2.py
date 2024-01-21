#좀비문제
import sys
sys.stdin = open('input.txt', 'r')


ability = [0]*3
time = [987654321]*1000

for i in range(3):
    a, b = map(int, input().split())
    ability[0], ability[1], ability[2] = map(int, input().split())

    q = []
    time[a] = 0

    def BFS(here):
        while q:
            here = q.pop(0)
            for i in range(3):
                Next = here + ability[i]
                if Next > len(time) -1: continue
                if time[Next] > time[here] + 1:
                    time[Next] = time[here] + 1
                    q.append(Next)

    if a == b: print(0)
    else:
        q.append(a)
        BFS(a)

    if time[b]!= 987654321 : print(time[b])
    else: print(-1)

    


