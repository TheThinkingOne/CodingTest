import sys
sys.stdin = open('input.txt', 'r')

Data = [list(map(int, input().split())) for _ in range (5)]

max = 0
sum = 0

for y in range(5):
    for x in range(5):
        sum+=Data[y][x]
        #만약 합이 max보다 크면 sum값을 max에 저장
        if sum > max : max = sum
    sum = 0 #여긴 왜 이렇게 해주는걸까? => 각각의 경우마다 초기화 해주기 위해서

for i in range(5):
    sum += Data[y][x]
    if sum > max : max = sum
print(max)
