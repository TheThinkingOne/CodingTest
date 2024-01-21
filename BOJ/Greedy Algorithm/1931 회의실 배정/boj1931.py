import sys
sys.stdin = open('input.txt','r')

startList = []
endList = []
schedules = []

N = int(input())
Visited = [[False] * N for _ in range(N)]

for i in range(N):
    A, B = map(int,input().split())
    startList.append([A,B])

# startList.sort(key=lambda x:x[0])
# startList.sort(key=lambda x:x[1])
# print(startList)

count = 1
end = startList[0][1]
# print(end)
for i in range(1, N):
        if startList[i][0] >= end:
            count += 1
            end = startList[i][1]


print(count)
# schedules.sort(key=lambda x:x[0])
# schedules.sort(key=lambda x:x[1])

# for j in range(N-1,-1,-1):
#     if endList[j] <= max(startList):
#
#
#     times = list(map(int,input().split()))
#     schedules.append(times)
# print(max(schedules))
# print(schedules[0])


# for j in range(N-1,-1,-1):
#     for k in range(N-1,-1,-1):
#         if schedules[j][0] >= schedules[0][k]:
# for j in range(N-1,-1,-1):
#     if

        # count = 0
        # if schedules[j][1] <= schedules[k][0]:
        #     j = k
        #     count += 1

# https://hongcoding.tistory.com/22

