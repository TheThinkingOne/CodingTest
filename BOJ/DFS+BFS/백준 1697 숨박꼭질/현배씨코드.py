#좀비문제랑 닮음
import sys
sys.stdin = open('input.txt', 'r')

n, k = map(int, input().split())
q = []
time = [987654321]*(300003)
time[n] = 0

#print(time)
def BFS():
    while q:
        here = q. pop(0)
        for i in (here+1, here-1, here*2):
            if 0 <= i < 300003:
                if time[i] > time[here] + 1:
                    time[i] = time[here] + 1
                    q.append(i)

if n == k: print(0)
else:
    q.append(n)
    BFS()
    if time[k]!= 987654321: print(time[k])

    



