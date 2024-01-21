import sys
sys.stdin = open('input.txt', 'r')

sum = 0
T = int(input())
for i in range(1,T+1):
    sum += i
print(sum)