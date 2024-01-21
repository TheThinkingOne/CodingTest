import sys
sys.stdin = open('input2.txt','r')

N, K = map(int, input().split())
cashValueList = [int(input()) for _ in range(N)]

result = 0

while K != 0:
    for j in range(N - 1, -1, -1):  # 가치가 큰 동전부터 탐색
        share = K // cashValueList[j]
        if share > 0:
            result += share
            K %= cashValueList[j]
            break

print(result)
