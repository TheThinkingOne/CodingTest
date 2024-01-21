import sys
sys.stdin = open('input.txt', 'r')

V, E = map(int, input().split())
print(V-E+1)