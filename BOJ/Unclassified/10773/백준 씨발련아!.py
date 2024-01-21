import sys
sys.stdin = open('백준씨발련아.txt', 'r')
N = int(sys.stdin.readline())
Save = []
for i in range(N):
    Data = list(map(int,sys.stdin.readline().split()))
    for k in Data:
        if k != 0:
            Save.append(k)
        else:
            Save.pop(-1)
if Save:
    print(sum(Save))
else:
    print(-1)
