import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
List = []
for i in range(N):
    num = int(input())
    List.append(num)
List.sort()
for i in List:
    print(i)