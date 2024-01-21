import sys
sys.stdin = open('input.txt','r')

T = int(input())
for i in range(T):
    j = int(input())
    for Pascal1 in range(1,j+1):
        if Pascal1 == '1' or Pascal1 == j + 1:
            Triangle = '1'
        else:
            Triangle = Pascal1
        print(Pascal1, end = ' ')

