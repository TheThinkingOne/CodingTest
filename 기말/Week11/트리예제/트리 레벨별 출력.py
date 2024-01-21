import sys

sys.stdin = open('input.txt', 'r')

V, E = map(int, input().split())

Tree = [[0] * 5 for _ in range(V + 1)]

for i in range(V):
    Tree[i][3] = Tree[i][4] = -1

Tree[1][4] = 0

Data = list(map(int, input().split()))

levelmax = 0

for i in range(E):

    parent, child = Data[i * 2], Data[i * 2 + 1]

    if Tree[parent][0] == 0:

        Tree[parent][0] = child

        Tree[parent][2] += 1

        Tree[child][3] = parent

        Tree[child][4] = Tree[parent][4] + 1  # 레벨

        if Tree[child][4] > levelmax:
            levelmax = Tree[child][4]

    else:

        Tree[parent][1] = child

        Tree[parent][2] += 1

        Tree[child][3] = parent

        Tree[child][4] = Tree[parent][4] + 1  # 레벨

        if Tree[child][4] > levelmax:
            levelmax = Tree[child][4]

for level in range(0, levelmax + 1):

    for i in range(0, V + 1):

        if Tree[i][4] == level:
            print(i, end=' ')

    print()