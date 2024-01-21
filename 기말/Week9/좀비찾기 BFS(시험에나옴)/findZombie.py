import sys
sys.stdin = open('input.txt', 'r') # 파일에서 읽을 때 사용

ability = [0]*3 # 짝수번째 줄의 갈수있는 길이 받을 것임
Time = [987654321]*1000 #

Queue = []

def BFS(here):
    while Queue: # 큐에 원소가 있는 동안 (큐에 1넣어져서 원소가 생김)
        here = Queue.pop(0)
        for i in range(3): # i=0,1,2
            next_ = here + ability[i] # + 2,5,7
            if next_ > len(Time)-1: continue
            if Time[next_] > Time[here] + 1: # 여러가지 경우에서 도달한 숫자가 같은 경우
                Time[next_] = Time[here] + 1
                Queue.append(next_)

for i in range(4):
    Shalala, Zombie = map(int, input().split()) # 1, 15
    ability[0], ability[1], ability[2] = map(int, input().split()) # 2, 5, 7

    Time[Shalala] = 0
    Queue.append(Shalala)
    BFS(Shalala) # shalala = 1 시작

    if Time[Zombie] != 987654321: # 경로에 간 곳에 있으면
        print(Time[Zombie])
    else: # 길이 연산을 통해 갔는데도 도달을 못 한다면
        print(-1)



