#현배씨코드
import sys
sys.stdin = open("input.txt", "r")

dx = [-1, 1, 0]
dy = [0, 0, -1]

def isSafe(y, x):
    if y >= 0 and x <= 99 and x >= 0:
        return True
    else:
        return False


def ladder(y, x):
    global answer

    for k in range(3):
        if answer != 0:
            return
        elif isSafe(y + dy[k], x + dx[k]):
            if mymap[y + dy[k]][x + dx[k]] == 1:
                mymap[y + dy[k]][x + dx[k]] = 0 #현재 출발지를 0으로 만들어서 다시 안 돌아가게 함
                ladder(y + dy[k], x + dx[k]) #다음 순서로 재귀
            elif y == 0:
                answer = x
                return


for i in range(10):
    answer = 0
    mymap = []
    n = int(input())
    for j in range(100):
        line = list(map(int, input().split()))
        mymap.append(line) #mymap 배열에 line 추가
        if 2 in line: #2가 라인에 있으면
            startx = line.index(2) #index 사용해서 2인 x자리 찾음
            starty = j #j는 99가 될것

    ladder(starty, startx)  #(99, 값이 2인 지점의 x)
    print("#%d %d" % (i + 1, answer))