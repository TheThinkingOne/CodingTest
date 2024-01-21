import sys
sys.stdin = open('input.txt', 'r')

sum = 0

Data = list(map(int, input()))
for i in range(len(Data)):
    sum += Data[i]
print(sum)