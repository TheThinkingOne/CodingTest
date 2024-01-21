import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for _ in range(T):
    days = int(input())
    stock = list(map(int, input().split()))

    max_price = 0
    totalBenefit = 0

    for i in range(days - 1, -1, -1):  # 주가를 거꾸로 탐색
        if stock[i] > max_price:
            max_price = stock[i]  # 최대 주가 갱신
        else:
            totalBenefit += max_price - stock[i]  # 최대 주가에서 현재 주가를 뺀 값을 이익에 추가

    print(totalBenefit)
