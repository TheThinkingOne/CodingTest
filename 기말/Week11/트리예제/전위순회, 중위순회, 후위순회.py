import sys

sys.stdin = open("input.txt", "r")

v, l = map(int, input().split())
nlist = list(map(int, input().split()))
data = [[0]*2 for i in range(v+1)]

for i in range(l):
    p, c = nlist[i*2], nlist[i*2+1]
    if data[p][0] == 0 :
        data[p][0] = c
    else:
        data[p][1] = c

for j in data:
    print(j)

def preorder(here): #전위순회
    if here:
        print("%d" % here, end=' ')
        preorder(data[here][0])
        preorder(data[here][1])

def inorder(here): #중위순회
    if here:
        inorder(data[here][0])
        print("%d" % here, end=' ')
        inorder(data[here][1])

def postorder(here): #후위순회
    if here:
        postorder(data[here][0])
        postorder(data[here][1])
        print("%d" % here, end=' ')
        
print("preorder")
preorder(1)
print()
print("inorder")
inorder(1)
print()
print("postorder")
postorder(1)
print()

