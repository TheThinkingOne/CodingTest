# import sys
# sys.stdin = open('input.txt', 'r')
#
# dy = [0,0,-1] #한칸 위로 가는거
# dx = [-1,1,0] #좌 우 상
#
# def isPossible(y,x):
#     if 0 <= y < 100 and 0 <= x < 100 and MyMap[y][x] == 1:
#         return True
#     else:
#         return False
#
# def GetSome(y,x):
#     MyMap[y][x] = -1
#     if y==0: #처음줄로 돌아가면
#         print("#%d " %tc, x)
#         return
#
#     for dir in range(3): #사다리 이동방향 상좌우 의 경우 3가지
#         newY = y+dy[dir]
#         newX = x+dx[dir]
#         if isPossible(newY,newX):
#             GetSome(newY, newX)
#             return #완전탐색을 하지 말라? BREAK랑 똑같은 뜻인가?
#             #위의 return 지워보고 답 다시 봐라
#             #위의 return을 안 쓰면 계속 돌게되는것
#
#
# #거꾸로가는 방법 사용
# for tc in range(1,11):
#     T = int(input())
#     MyMap = [[0 for x in range(100)] for y in range(100)]
#     for y in range(100):
#         MyMap[y] = list(map(int, input().split()))
#     for x in range(100):
#         if MyMap[99][x] == 2: #맨 끝에서 2인 지점이 있으면 찾아서 이걸 스타트 지점으로 함
#             startX = x
#         x = startX
#         y = 99
#
#     GetSome(y,x)

#구글바드 수정본
import sys
sys.stdin = open('input.txt', 'r')

dy = [0, 0, -1]  # 한칸 위로 가는거
dx = [-1, 1, 0]  # 좌 우 상

def isPossible(y, x):
    if 0 <= y < 100 and 0 <= x < 100 and MyMap[y][x] != 0:
        return True
    else:
        return False

def GetSome(y, x):
    MyMap[y][x] = -1
    global startX
    if y == 0:  # 처음줄로 돌아가면
        print("#%d " % tc, x)
        return

    for dir in range(len(dy)):  # 사다리 이동방향 상좌우 의 경우 3가지
        newY = y + dy[dir]
        newX = x + dx[dir]
        if isPossible(newY, newX):
            startX = x
            GetSome(newY, newX)
            return


# 거꾸로가는 방법 사용
for tc in range(1, 11):
    T = int(input())
    MyMap = [[0 for x in range(100)] for y in range(100)]
    for y in range(100):
        MyMap[y] = list(map(int, input().split()))
    for x in range(100):
        if MyMap[99][x] == 2:  # 맨 끝에서 2인 지점이 있으면 찾아서 이걸 스타트 지점으로 함
            global startX
            startX = x
        x = startX
        y = 99

    GetSome(y, x)






