import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for i in range(T):
    Hour1, Minute1, Hour2, Minute2 = map(int, input().split())
    MinSum = 0
    HourSum = 0
    for j in range(T):
        MinSum = Minute1 + Minute2
        HourSum = Hour1 + Hour2
        if MinSum >= 60:
            MinSum -= 60
            HourSum += 1
        if HourSum > 12:
            HourSum -= 12
    print(f"#{i+1} {HourSum} {MinSum}")