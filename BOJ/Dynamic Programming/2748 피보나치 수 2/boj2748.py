import sys
sys.stdin = open('input.txt')

N = int(input())

memo = {}

def Fibonachi(current, N):
    if current <= 1:
        return current

    if current not in memo:
        memo[current] = Fibonachi(current - 1, N) + Fibonachi(current - 2, N)

    return memo[current]

result = Fibonachi(N, N)
print(result)




