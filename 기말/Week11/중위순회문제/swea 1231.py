import sys
sys.stdin = open('input.txt', 'r')

def inorder(here):
    if here:
        inorder(Tree[here][0]) #왼쪽자식
        print(dic[str(here)], end='')
        inorder(Tree[here][1]) #오른쪽자식

for TC in range(10):
    N = int(input())
    Tree = [[0]*2 for __ in range(N+1)]
    dic = {}
    for i in range(N):
        Info = list(input().split())
        dic[Info[0]] = Info[1]
        if len(Info) == 4:
            Tree[int(Info[0])][0] = int(Info[2])
            Tree[int(Info[0])][1] = int(Info[3])
        elif len(Info) == 3:
            Tree[int(Info[0])][0] = int(Info[2])
        #len(Info)가 2일땐 추가 작업 필요없음

    print(f"#{TC+1}", end=' ')
    inorder(1)
    print()

# import sys
# sys.stdin = open('input.txt','r')
# # Define the function for inorder traversal
# def inorder(here, Tree, dic):
#     if here:
#         inorder(Tree[here][0], Tree, dic)  # Left child
#         print(dic[str(here)], end='')  # Current node
#         inorder(Tree[here][1], Tree, dic)  # Right child
#
# # Set the path to the input file
#
#
# # Read and process each test case
# for TC in range(10):
#     N = int(input())
#     Tree = [[0]*2 for __ in range(N+1)]
#     dic = {}
#
#     # Read each node's information
#     for _ in range(N):
#         Info = input().split()
#         node_num = int(Info[0])
#         dic[Info[0]] = Info[1]
#         if len(Info) > 2:
#             Tree[node_num][0] = int(Info[2])  # Left child
#         if len(Info) > 3:
#             Tree[node_num][1] = int(Info[3])  # Right child
#
#     # Perform inorder traversal and print the output
#     print(f"#{TC+1}", end=' ')
#     inorder(1, Tree, dic)
#     print()
