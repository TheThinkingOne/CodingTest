import sys
sys.stdin = open('input.txt', 'r')

t = int(input())

def BFS(here): #here =1로 시작
    global g, flag 
    while q:
        here = q.pop(0)
        for i in range(v): #v=6
            if i == g and mymap[here][i] == 1:
                time[i] = time[here] + 1
                flag = 1
                return
            elif mymap[here][i] == 1 and visited[i] == 0:
                time[i] = time[here] + 1
                q.append(i)
                visited[i] = 1
                    
for i in range(t):
    v, e = map(int, input().split()) #6,5
    mymap = []
    visited = [0]*v
    time = [0]*v
    q = []
    flag = 0
    
    for k in range(v): #v=6
        mymap.append([0]*v)

    for j in range(e): #e=5
        v1, v2 = map(int, input().split())
        v1 -= 1
        v2 -= 1
        mymap[v1][v2] = 1
        mymap[v2][v1] = 1

    s, g = map(int, input().split()) #s=1, v= 6
    s -= 1
    g -= 1
    visited[s] = 1
    q.append(s)
    BFS(s)
    print("#%d" %(i+1), end = " ")
    if flag == 1:
        print(time[g])
    else:
        print(0)

    
    
        
        
    
