import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
result = ''

for i in range(T):
    V, E = map(int, input().split())
    if V == E:
        result = '='
    elif V > E:
        result = '>'
    elif V < E:
        result = '<'
    print(f"#{i+1} {result}")