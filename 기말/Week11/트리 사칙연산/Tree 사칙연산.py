import sys
sys.stdin = open('input.txt.txt', 'r')
#in-order

def postorder(here):
    if here:
        a = postorder(Tree[here][1])
        b = postorder(Tree[here][2])

        if str(Tree[here][0]) in '+-/*':
            if Tree[here][0] == "+":
                return a+b
            elif Tree[here][0] == "-":
                return a-b
            elif Tree[here][0] == "/":
                return a/b
            elif Tree[here][0] == "*":
                return a*b
        else:
            return Tree[here][0]

for TC in range(10):
    N = int(input())
    Tree = [[0]*3 for __ in range(N+1)]
    # dic = {}
    for i in range(N):
        Info = list(input().split())
        # dic[Info[0]] = Info[1]
        if Info[1] in '+-*/':
            Tree[int(Info[0])][0] = Info[1]
            Tree[int(Info[0])][1] = int(Info[2])
            Tree[int(Info[0])][2] = int(Info[3])
        else:
            Tree[int(Info[0])][0] = int(Info[1])

    answer = postorder(1)
    print(f"#{TC+1} {int(answer)}")