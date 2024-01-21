import sys

sys.stdin = open('input.txt', 'r')

howmany = int(input())

for tc in range(howmany):
    Data = list(map(int, input().split()))

    max_val = Data[0]
    for num in Data:
        if num > max_val:
            max_val = num

    print(f"#{tc + 1} {max_val}")

