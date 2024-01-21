import sys
sys.stdin = open('input.txt', 'r')

Fontaine = []
Dissoluted = []
N, K = map(int, sys.stdin.readline().split())
idx = K-1

for i in range(1,N+1):
    Fontaine.append(i)

while len(Fontaine) > 0:
    idx = idx % len(Fontaine)

    Dissoluted.append(Fontaine.pop(idx))
    idx += K-1

print('<' + ', '.join(map(str, Dissoluted)) + '>')


    # for j in range(len(Fontaine)): # 0~6
    #     if (j+1)%K == 0:
    #         Survived.append(Fontaine.pop(j))
    #     else:
    #         Fontaine.pop(j)
