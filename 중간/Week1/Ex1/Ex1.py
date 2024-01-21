import sys

sys.stdin = open('input.txt', 'r')

howmany = int(input())

for tc in range(howmany):
    what = int(input())
    print(f"#{tc+1} {what}")