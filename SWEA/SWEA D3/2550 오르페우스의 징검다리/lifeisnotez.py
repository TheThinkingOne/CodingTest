import sys
sys.stdin = open('input.txt','r')

T = int(input())
played = 0
def moveAlong(currentPoint, change): #각 발판의 목숨도 생각해야함
    global played
    while sum(leg) == len(leg):
        for i in range(currentPoint, len(leg)):
            if leg[i-1] == 1 and leg[i+1] == 0:
                currentPoint = i
                for l in range(currentPoint, currentPoint + change+1):
                    if leg[l] == '0':
                        leg[l] += 1
                    elif leg[l] == '1':
                        leg[l] -= 1
                    played += 1
                    moveAlong(l, change)
    else:
        played = -1

for i in range(T):
    played = 0
    leg = list(input())
    change, life = map(int,input().split())
    eachLife = [[life]* len(leg)]
    for j in range(len(leg)):
        if leg[0] == '0':
            currentPoint = 0 # i=0일떼 i-1인거 수정해야함
            moveAlong(currentPoint, change)
        elif leg[0] == '1':
            for k in range(1, len(leg)):
                if leg[k - 1] == 1 and leg[k + 1] == 0:
                    currentPoint = k
                    moveAlong(currentPoint, change)
    print(f"{i+1} {played}")
