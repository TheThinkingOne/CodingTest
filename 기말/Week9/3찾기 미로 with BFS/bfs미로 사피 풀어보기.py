import sys
sys.stdin = open('input.txt', 'r')
t = int(input())

for i in range(t):
    n = int(input())
    mymap = [["1"]*(n+2)]
    q = []
    dy = [-1, 1, 0, 0] 
    dx = [0, 0, -1, 1]
    flag = 0
    
    for j in range(n):
        lineList = ["1"]
        line = input()
        for k in line:
            lineList.append(k)
        if "2" in lineList:
            startx = lineList.index("2")
            starty = j
            q.append([starty+1, startx])
        lineList.append("1")
        mymap.append(lineList)
    mymap.append(["1"]*(n+2))
    
    while q:
        y, x = q.pop(0)
        for j in range(4):
            if mymap[y + dy[j]][x + dx[j]] == "0":
                q.append([y + dy[j], x + dx[j]])
                mymap[y + dy[j]][x + dx[j]] = "1"
            elif mymap[y + dy[j]][x + dx[j]] == "3":
                flag = 1
                break

    print("#%d %d" %(i+1, flag))
    
    

    
    
    
