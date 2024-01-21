import sys
sys.stdin = open('input.txt','r')

TC = int(input())

for _ in range(TC):
    N, M = map(int,input().split())
    #N=문서의 개수 M=목표 문서의 큐에 놓인 순서(맨 왼쪽이 0번쨰)
    Priority = list(map(int,input().split()))
    target = Priority[M]
    count = 0
    while True:
        if Priority[0] == max(Priority):
            if Priority[0] == target and Priority.index(target) == 0:
                count += 1
                print(count)
                break
            else:
                Priority.pop(0)
                count += 1

        elif Priority[0] != max(Priority):
            temp = Priority[0]
            Priority.append(temp)
            Priority.pop(0)




