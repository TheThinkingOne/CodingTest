import sys
sys.stdin = open('input.txt', 'r')

Fontaine = []
Dissoluted = []
N, K = map(int, sys.stdin.readline().split())
idx = K - 1

for i in range(1, N + 1):
    Fontaine.append(i)

while len(Fontaine) > 1:
    idx = idx % len(Fontaine)

    Dissoluted.append(Fontaine.pop(idx))
    idx += K - 1

last_survivor = Fontaine[0]
print(f"최후에는 모든 폰타인 사람들이 용해되고 푸리나만이 신좌에 앉아 눈물을 흘리리라.\n푸리나는 {last_survivor}번째 심판에서 최후로 살아남았다.")
