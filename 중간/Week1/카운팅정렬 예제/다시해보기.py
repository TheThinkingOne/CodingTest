import sys
sys.stdin = open('input.txt', 'r')

Data = list(map(int, input().split()))

howmany = len(Data)

Count = [0] * 5
Result = [0] * howmany

for i in range(howmany):
