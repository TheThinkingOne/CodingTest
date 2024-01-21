import sys
sys.stdin = open('input.txt','r')

#자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는
# 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

N, M = map(int,input().split())
NList = []

for i in range(N):
    NList.append(i+1)

Visited = [False] * (N+1)
result = [0] * M
#print(NList)

def DFS(here):
    if here == M: #현재 값이 M이 되면 출력하고 종료
        print(" ".join(map(str,result)))
        return

    for i in range(1,N+1):
        if not Visited[i]:
            Visited[i] = True
            result[here] = i
            DFS(here+1)
            Visited[i] = False

DFS(0)



    # for next in NList[here]:
    #     if not Visited[next]:
    #         DFS(next)



