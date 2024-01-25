import sys
sys.stdin = open('input.txt','r')

MyMap = []

H, W, X, Y = map(int,input().split())
#H=세로, W=가로
#X=2 Y=1
for _ in range(H+X):
    nums = list(map(int,input().split()))
    MyMap.append(nums)
#print(MyMap)
#print(MyMap[X][Y]) = MyMap[2][1] = 9
#print(MyMap[W-Y][H-X])

for i in range(X,H):
    for j in range(Y,W):
        MyMap[i][j] -= MyMap[i-X][j-Y]

for y in range(H):
    for x in range(W):
        print(MyMap[y][x],end=" ")
    print()



#아래로 X칸, 오른쪽으로 Y칸
#MyMap = [[0] * (W+Y) for _ in range(H+X)]
# for _ in range(H+W):
#     MyMap.append(input().split())
# print(MyMap)