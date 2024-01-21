import sys
from itertools import permutations
sys.stdin = open('input.txt','r')

data = ['1','2','3','4','5','6','7','8','9']
number = list(permutations(data,3))
print(number)

N = int(input())
for _ in range(N):
    num, strike, ball = map(int,input().split())
    num = list(str(num))
    count = 0
    for i in range(len(num)):
        S, B = 0, 0
        i -= count
        for j in range(3):
            if number[i][j] == num[j]:
                S += 1
            elif num[j] in number[i]:
                B += 1

        if (S != strike) or (B != ball):
            number.remove(number[i])
            count += 1

print(len(number))

