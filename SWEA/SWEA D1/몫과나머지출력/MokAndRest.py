import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for i in range(T):
    V, E = map(int, input().split())
    print(f"#{i+1} {V//E} {V%E}")