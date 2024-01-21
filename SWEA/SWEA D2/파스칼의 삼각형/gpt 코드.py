import sys
sys.stdin = open('input.txt','r')

T = int(input())
for i in range(T): # i = 1
    j = int(input()) # j = 4
    row = [1]
    for k in range(max(j,1)):
        print(' '.join(map(str, row)))
        row = [1] + [row[l] + row[l + 1] for l in range(len(row) - 1)] + [1]