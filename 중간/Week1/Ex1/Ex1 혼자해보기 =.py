import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(T):
    num = int(input())
    print(f"#{tc} {num}")