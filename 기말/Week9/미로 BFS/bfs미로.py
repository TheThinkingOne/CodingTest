import sys
sys.stdin = open("input.txt", "r")
row, col = map(int, input().split()) # row, col = 5
mymap = []
q = []
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
flag = 0

for i in range(row): # row =5
    lineList = [] #미로 자체를 저장할 리스트
    line = input() #미로 한줄씩 불러오기
    for j in line: # j는 미로 한줄씩
        lineList.append(j)
    if 'S' in lineList:
        startx = lineList.index('S')
        starty = i
        q.append([starty, startx]) #큐에 시작점 저장
    mymap.append(lineList)

while q: #큐가 비어있는 동안
    y, x = q.pop(0) # y,x는 현위치 팝한것
    for j in range(4):
        try:
            if mymap[y + dy[j]][x + dx[j]] == ".": #dy[0] = -1, dx[0] = 0, ..... 위에 dx,dy참조
                q.append([y + dy[j], x + dx[j]])
                mymap[y + dy[j]][x + dx[j]] = "#" #갔던곳은 #으로 변경처리(되돌아가는것 방지)
            elif mymap[y + dy[j]][x + dx[j]] == "G": #도착
                flag = 1
        except:
            continue

if flag == 1:
    print("도착")
else:
    print("길잃음")



