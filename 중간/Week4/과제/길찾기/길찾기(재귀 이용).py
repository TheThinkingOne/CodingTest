import sys
sys.stdin = open('input.txt', 'r')
#
# for tc in range(1,11):
#     V, E = map(int, input().split())
#     start, stop = list(map(int, input().split()))

def DFS(here):
    Visited[here] = 1

    for next in range(100):
        if MyMap[here][next] and not Visited[next]:
            DFS(next)

for n in range(10):
    MyMap = [[0 for _ in range(100)] for __ in range(100)]
    Visited = [0] * 100
    V, E = map(int, input().split())

    for _ in range(E):
        Data = list(map(int, input().split()))
        for i in range(0, E * 2, 2):
            if i <= (E * 2):
                start, stop = Data[i], Data[i + 1]
                MyMap[start][stop] = 1
        break
    DFS(0)

    print(f"#{V} {Visited[99]}")

# import sys
# sys.stdin = open('input.txt', 'r')
#
# def DFS(here):
#     Visited[here] = 1
#
#     for next in range(100):
#         if MyMap[here][next] and not Visited[next]:
#             DFS(next)
#
# for tc in range(10):
#     MyMap = [[0 for _ in range(100)] for __ in range(100)]
#     Visited = [0] * 100  # 갔는지 안갔는지 표시하는 것
#     V, E = map(int, input().split())
#
#     for i in range(E):
#         Data = list(map(int, input().split()))
#         for j in range(0, E * 2, 2):
#             if j <= (E * 2):
#                 start, stop = Data[j], Data[j+1]
#                 MyMap[start][stop] = 1
#             break
#     DFS(0)
#
#     print(f"#{V} {Visited[99]}")

# def DFS(here):
#     Visited[here] = 1
#
#     for next in range(100):
#         if MyMap[here][next] and not Visited[next]:
#             DFS(next)
#
# with open('input.txt', 'r') as file:
#     lines = file.readlines()
#
# # 각 테스트 케이스를 처리
# for n in range(10):
#     V, E = map(int, lines[n * 2].split())  # 첫 줄에서 V와 E를 읽어옴
#
#     # 그래프와 방문 여부를 초기화
#     MyMap = [[0 for _ in range(100)] for __ in range(100)]
#     Visited = [0] * 100
#
#     # 간선 정보를 읽어와서 그래프를 생성
#     edges = list(map(int, lines[n * 2 + 1].split()))
#     for i in range(0, E * 2, 2):
#         start, stop = edges[i], edges[i + 1]
#         MyMap[start][stop] = 1
#
#     DFS(0)
#
#     print(f"#{V} {Visited[99]}")

    ######################################교수님풀이

    # def DFS2(here):
    #     Visited2[here] = 1 #방문한곳은 1로 바꿔서 거기로 다시 안 돌아가게
    #
    #     for next in range(100):
    #         if MyMap2[here][next] and not Visited2[next]: #길이 있고 방문한 적이 없으면 간다
    #             DFS2(next)
    #
    # for num in range(10):
    #     MyMap2 = [[0 for alpha in range(100) for beta in range(100)]]
    #     tc, howmany = map(int,input().split())
    #     Data = list(map(int, input().split()))
    #     Visited2 = [0] * 100 #방문한곳은 갈때마다 1로 바꿈(
    #
    #     for k in range(howmany): #edge 수 받아옴
    #         Start, Stop = Data[k*2], Data[k*2+1] #짝수번째 줄에서 홀수번째는 시작, 짝수번째는 가는곳
    #         MyMap2[Start][Stop] = 1
    #
    #     DFS2(0)
    #     print(f"#{tc}, {Visited2[99]}")





