import sys
sys.stdin = open('input.txt', 'r')

#거꾸로가는 방법 사용
for tc in range(1,11):
    input() #레더 앞서 나오는 숫자들 읽어오기
    MyMap = [[0 for x in range(100)] for y in range(100)]

    for y in range(100):
        MyMap[y] = list(map(int, input().split()))
    for x in range(100):
        if MyMap[99][x] == 2: #맨 끝에서 2인 지점이 있으면 찾아서 이걸 스타트 지점으로 함
            startX = x
    x = startX
    y = 99

    while True:
        #왼쪽으로 이동경로 있는지 파악
        if(x-1) >= 0 and MyMap[y][x-1]==1:
            while (x-1) >= 0 and MyMap[y][x-1]==1:
                x-=1
            y-=1
        #오른쪽으로 이동경로 있는지 파악
        elif (x+1) < 100 and MyMap[y][x+1] == 1:
            while (x+1) < 100 and MyMap[y][x+1] == 1:
                x+=1
            y-=1
        else:
            #왼쪽오른쪽 둘다 경로가 없을경우
            y-=1 #위로 올라가므로 y값 1줄임
        if y==0: break
    print("#%d" %tc, x)