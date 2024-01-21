import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
Datas = list(map(int, input().split()))
medianVal = 0

for i in range(T):
    for j in range(len(Datas)):
        for k in range((len(Datas)-1)):
            if Datas[k] > Datas[k+1]:
                Datas[k], Datas[k + 1] = Datas[k + 1], Datas[k]
print(Datas[99])
# FindMedian(T)
#
# def FindMedian(T):
#     if T % 2 == 0:
#         medianVal = ((Datas[T/2] + Datas[T/2+1])) / 2
#     elif T % 2 == 1:
#         medianVal = ((Datas[T/2 + 0.5]))
#
# print(Datas[99])



