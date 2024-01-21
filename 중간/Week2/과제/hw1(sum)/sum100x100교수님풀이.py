import sys

sys.stdin = open("input100x100.txt", "r")

for i in range(10):
    num = int(input())
    box = []
    sumNlist = []

    for j in range(100):
        line = list(map(int, input().split()))
        sumN = sum(line)  # 가로덧셈
        sumNlist.append(sumN)
        box.append(line)

    for k in range(100):  # 세로덧셈
        sumN = 0
        for q in range(100):
            sumN += box[q][k]
        sumNlist.append(sumN)

    sumN = 0
    for w in range(100):  # 대각선덧셈
        sumN += box[w][w]
    sumNlist.append(sumN)

    sumN = 0
    for w in range(100):
        sumN += box[w][99 - w]
    sumNlist.append(sumN)

    maxN = max(sumNlist)

    print("#%d %d" % (num, maxN))