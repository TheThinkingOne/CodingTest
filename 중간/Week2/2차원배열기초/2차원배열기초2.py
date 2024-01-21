import sys
sys.stdin = open('input.txt', 'r')

Data = [list(map(int, input().split())) for i in range(5)]

max = 0
sum = 0

for y in range(5):
    for x in range(5): #행별로 더하기
        sum+=Data[y][x]
        if sum > max: max = sum
        print(sum)
    sum = 0

#대각선 합
sum =0
for i in range(5):
    sum+=Data[i][i]
    print(sum)
if sum > max: max = sum

print(max)