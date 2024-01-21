import sys

sys.stdin = open('input.txt', 'r')

startList = []
endList = []

N = int(input())

for i in range(N):
    A, B = map(int, input().split())
    startList.append(A)
    endList.append(B)

# 시작 시간이 가장 늦은 순서로 정렬
sorted_indices = sorted(range(N), key=lambda k: startList[k], reverse=True)

count = 1
end = endList[sorted_indices[0]]

# 가장 늦게 시작하는 회의부터 반대로 순회하면서 겹치지 않는 회의 선택
for i in range(1, N):
    if startList[sorted_indices[i]] >= end:
        count += 1
        end = endList[sorted_indices[i]]

print(count)

