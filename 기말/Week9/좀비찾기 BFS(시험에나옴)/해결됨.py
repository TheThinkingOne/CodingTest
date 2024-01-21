import sys
sys.stdin = open('input.txt', 'r') # 파일에서 읽을 때 사용

ability = [0]*3 # 짝수번째 줄의 갈수있는 길이 받을것임
Time = [987654321]*1000 #

# Shalala, Zombie = map(int,input().split()) # 1, 15
# ability[0], ability[1], ability[2] = map(int, input().split()) # 2, 5, 7

Queue = []

def BFS(here):
    while Queue: #큐에 원소가 있는 동안 (큐에 1넣어져서 원소가 생김)
        here = Queue.pop(0)
        for i in range(3): # i=0,1,2
            next = here + ability[i] # + 2,5,7
            if next < 0 or next > len(Time)-1: continue
            # next가 범위를 벗어나는지 체크
            if Time[next] > Time[here] + 1: #여러가지 경우에서 도달한 숫자가 같은 경우
                Time[next] = Time[here] + 1
                Queue.append(next)

for i in range(4):
    Shalala, Zombie = map(int,input().split()) # 1, 15
    ability[0], ability[1], ability[2] = map(int, input().split()) # 2, 5, 7

    Time[Shalala] = 0
    if Shalala == Zombie :
        print(0)
        continue
    else:
        Queue.append(Shalala)
        BFS(Shalala) #shalala = 1 시작


    if Time[Zombie]!=987654321:
        print(Time[Zombie]) # 경로에 간 곳에 있으면
    else:
        print(-1) # 길이 연산을 통해 갔는데도 도달을 못 한다면


