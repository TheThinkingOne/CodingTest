import sys
sys.stdin = open('input.txt','r')

N = int(input())
ropeList = []

for _ in range(N):
    rope = int(input())
    ropeList.append(rope)

ropeList.sort()  # 로프를 버틸 수 있는 중량을 오름차순으로 정렬

max_weight = 0
for i in range(N): #i=0~4
    max_weight = max(max_weight, ropeList[i] * (N - i))  # 선택한 로프 중 가장 약한 로프의 중량 * 선택한 로프의 수
    # i=0 -> 50 , i=1 ->
    # max_weight = max(max_weight, ropeList[i] * (N - i)): 선택한 로프 중 가장 약한 로프의 중량(ropeList[i])에 현재 선택한 로프 개수(N - i)를 곱한 값과 max_weight 중 더 큰 값을 max_weight에 저장합니다.
print(max_weight)
