import sys
sys.stdin = open('input.txt', 'r')

#ㅌ리 구조 출력
V, E = map(int, input().split()) # V = 13, E = 12

Tree = [[0]*2 for __ in range(V+1)]
#트리

Data = list(map(int, input().split()))
for i in range(E):
    parent, child = Data[2*i], Data[2*i+1] #parent =1
    if Tree[parent][0] == 0:
        Tree[parent][0] = child
    else:
        Tree[parent][1] = child

print(Tree)