import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for _ in range(T):
    days = int(input())
    stock = list(map(int, input().split()))

    totalBenefit = 0
    while stock:  # 주식 정보가 남아있는 동안 반복
        max_price = max(stock)
        max_index = stock.index(max_price)

        if max_index == 0:  # 첫 번째 날의 주가가 최대일 경우
            stock = stock[1:]  # 첫 번째 날의 주식 정보를 제거하고 다시 반복
            continue

        totalBenefit += max_price * max_index  # 최대 주가를 기준으로 이익 계산
        totalBenefit -= sum(stock[:max_index])  # 최대 주가 이전의 주식 매도
        stock = stock[max_index + 1:]  # 최대 주가 이후의 주식 정보만 남김

    print(totalBenefit)


