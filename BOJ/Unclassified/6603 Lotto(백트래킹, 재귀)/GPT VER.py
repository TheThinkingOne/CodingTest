from itertools import combinations
import sys
sys.stdin = open('input.txt', 'r')

while True:
    Data = list(map(int, sys.stdin.readline().split()))
    K = Data[0]
    if K == 0: break

    Stack = Data[1:]
    result = list(combinations(Stack, 6))

    for combo in result:  # 변수 이름을 combinations에서 다른 이름으로 수정
        print(' '.join(map(str, combo)))
    print()


