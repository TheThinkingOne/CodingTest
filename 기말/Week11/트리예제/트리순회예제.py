import sys
sys.stdin = open('input.txt', 'r')

V, E = map(int, input().split()) # V = 13, E = 12

Tree = [[0]*2 for __ in range(V+1)]

Data = list(map(int, input().split()))

def preorder(here):
    if here:
        print("%d" %here, end=' ')
        preorder(Tree[here][0]) #왼쪽자식
        preorder(Tree[here][1]) #오른쪽자식

def inorder(here):
    if here:
        preorder(Tree[here][0]) #왼쪽자식
        print("%d" % here, end=' ')
        preorder(Tree[here][1]) #오른쪽자식

def postorder(here):
    if here:
        preorder(Tree[here][0]) #왼쪽자식
        preorder(Tree[here][1]) #오른쪽자식
        print("%d" % here, end=' ')


for i in range(E):
    parent, child = Data[2*i], Data[2*i+1] #parent =1
    if Tree[parent][0] == 0:
        Tree[parent][0] = child
    else:
        Tree[parent][1] = child

preorder(1)
print("\n")
inorder(1)
print("\n")
postorder(1)