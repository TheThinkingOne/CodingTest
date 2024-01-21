import sys
sys.stdin = open('input.txt', 'r')

def count_possible_coordinates(x1, y1, r1, x2, y2, r2):
    distance_squared = (x2 - x1) ** 2 + (y2 - y1) ** 2
    distance = distance_squared ** 0.5

    if distance == 0 and r1 == r2:  # 무한대의 경우
        return -1
    elif distance > r1 + r2 or distance + min(r1, r2) < max(r1, r2):  # 교차하지 않는 경우
        return 0
    elif distance == r1 + r2 or distance + min(r1, r2) == max(r1, r2):  # 외접 또는 내접하는 경우
        return 1
    else:  # 두 점에서 만나는 경우
        return 2

N = int(input())
for i in range(N):
    Data = list(map(int, input().split()))
    result = count_possible_coordinates(Data[0], Data[1], Data[2], Data[3], Data[4], Data[5])
    print(result)
