# import sys
# sys.stdin = open('input.txt','r')
#
# TC = int(input()) # T = 10
# for killFlies in range(TC):
#     ArraySize, flapper = map(int, input().split())
#     Data = [list(map(int, input().split())) for _ in range (ArraySize)]
#     for y in range(ArraySize - flapper +1):
#         for x in range(ArraySize - flapper +1):
#             Sums = []
#             for j in range(y, y + flapper):
#                 for k in range(x, x + flapper):
#                     Sums.append(Data[j][k])
#             print(max(Sums))
import sys
sys.stdin = open('input.txt','r')

TC = int(input()) # T = 10
for killFlies in range(TC):
    ArraySize, flapper = map(int, input().split())
    Data = [list(map(int, input().split())) for _ in range(ArraySize)]
    max_sum = 0
    Sums = []
    for y in range(ArraySize - flapper + 1):
        for x in range(ArraySize - flapper + 1):
            ArraySum = 0
            for j in range(y, y + flapper):
                for k in range(x, x + flapper):
                    ArraySum += Data[j][k]
                    Sums.append(ArraySum)
            max_sum = max(Sums)
    print(f"#{killFlies+1} {max_sum}")

# import sys
# sys.stdin = open('input.txt','r')
#
# TC = int(input()) # T = 10
# for killFlies in range(TC):
#     ArraySize, flapper = map(int, input().split())
#     Data = [list(map(int, input().split())) for _ in range(ArraySize)]
#     max_sum = 0
#     for y in range(ArraySize - flapper + 1):
#         for x in range(ArraySize - flapper + 1):
#             ArraySum = 0
#             for j in range(y, y + flapper):
#                 for k in range(x, x + flapper):
#                     ArraySum += Data[j][k]
#             max_sum = max(max_sum, ArraySum)
#     print(max_sum)

