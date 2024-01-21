import sys
sys.stdin = open('input.txt', 'r')

V, E = map(int, sys.stdin.readline().split())  # V = 13, E = 12
Tree = [[0]*2 for __ in range(V+1)]

Data = list(map(int, sys.stdin.readline().split()))

def preorder(here):
    if here:
        print("%d" % here, end=' ')
        preorder(Tree[here][0])  # 왼쪽 자식 노드를 먼저 방문
        preorder(Tree[here][1])  # 오른쪽 자식 노드를 방문

def inorder(here):
    if here:
        inorder(Tree[here][0])  # 왼쪽 자식 노드를 방문
        print("%d" % here, end=' ')
        inorder(Tree[here][1])  # 오른쪽 자식 노드를 방문

def postorder(here):
    if here:
        postorder(Tree[here][0])  # 왼쪽 자식 노드를 방문
        postorder(Tree[here][1])  # 오른쪽 자식 노드를 방문
        print("%d" % here, end=' ')


for i in range(E):
    parent, child = Data[2*i], Data[2*i+1]  # parent = 1
    if Tree[parent][0] == 0:
        Tree[parent][0] = child
    else:
        Tree[parent][1] = child

print("Preorder Traversal:")
preorder(1)
print("\n")

print("Inorder Traversal:")
inorder(1)
print("\n")

print("Postorder Traversal:")
postorder(1)

