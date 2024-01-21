# import sys
# import math
# sys.stdin = open('input.txt','r')
#
# def isPrime(k):
#     if k <= 1:
#         return False
#     for i in range(2, int(k ** 0.5) + 1):  # 2부터 number의 제곱근까지의 수로 나눠보면 됨
#         if k % i == 0:  # 나누어 떨어지는 경우 소수가 아님
#             return False
#     return True
#
# TC = int(input())
# for i in range(TC):
#     A, B = map(int, input().split())
#     if A == B:
#         result = 0
#     elif A < B:
#         A, B = B, A
#
#     maxCount = float('inf')
#     result = 0
#
#
#     # count = 0
#     # maxCount = float('inf')
#     # k = 10**18
#     # while 0 <= A <= 10**18 and 0 <= B <= 10**18:
#     #     while A!=B:
#     #         A += isPrime(k)
#     #         count += 1
#     #         B -= isPrime(k)
#     #         count += 1
#     #         maxCount = min(maxCount, count)
#     #     else:
#     #         maxCount = -1
#     #     print(f"{i+1} {maxCount}")
import sys
sys.stdin = open('input.txt','r')
import math

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def maxOperations(A, B):
    count = 0
    while A != B:
        if A > B:
            found = False
            for i in range(A - B, 1, -1):
                if isPrime(i) and A % i == 0:
                    A -= i
                    count += 1
                    found = True
                    break
            if not found:
                return -1
        else:
            found = False
            for i in range(B - A, 1, -1):
                if isPrime(i) and B % i == 0:
                    B -= i
                    count += 1
                    found = True
                    break
            if not found:
                return -1

    return count

# 입력 처리 및 결과 출력
T = int(input())
for case in range(1, T + 1):
    A, B = map(int, input().split())
    result = maxOperations(A, B)
    print(f"#{case} {result}")







