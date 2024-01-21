import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for _ in range(T):
    V, E = map(int,input().split())
    print(V+E)