import sys
sys.stdin = open('input.txt', 'r')

test = int(input())
for i in range(test):
    count = int(input())
    nlist = list(map(int, input().split()))
    ndict = {}

    for j in nlist: #j는 nlist의 요소들을 불러옴
        if j in ndict:
            ndict[j] += 1
        else:
            ndict[j] = 1

    keylist = list(ndict.keys())
    valuelist = list(ndict.values())
    maxN = max(valuelist)
    maxNindex = valuelist.index(maxN)

    print("#%d %d" % (count, keylist[maxNindex]))