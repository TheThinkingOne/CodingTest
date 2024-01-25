import sys
sys.stdin = open('input.txt','r')

N = int(sys.stdin.readline())
list = []
for i in range(N):
    num = int(sys.stdin.readline())
    list.append(num)

list.sort()
for i in list:
    print(i)
