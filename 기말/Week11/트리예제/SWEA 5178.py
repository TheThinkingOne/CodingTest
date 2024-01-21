import sys
sys.stdin = open('input5178.txt', 'r')

def preorderCount(here):
    global Count
    if here:
        Count += 1
        preorderCount(Tree[here][0]) #왼쪽자식
        preorderCount(Tree[here][1]) #오른쪽자식

T = int(input())
for i in range(T):
    V, E = map(int, input().split())
    Data = list(map(int, input().split()))
    Tree = [[0]*2 for __ in range(1002)]
    # E의 자식에 속한 노드 개수 구하기
    Count = 0
    for k in range(V):
        parent, child = Data[2*k], Data[2*k+1]
        #트리 구리는 코드 부분
        if Tree[parent][0] == 0: #자식을 왼쪽부터 채움
            Tree[parent][0] = child
        else:
            Tree[parent][1] = child  #왼쪽에 사람있으면 오른쪽에 채움

    preorderCount(E)
    print(f"#{i+1} {Count}")
