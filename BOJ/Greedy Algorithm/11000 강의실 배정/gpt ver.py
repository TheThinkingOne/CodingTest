import heapq
import sys
sys.stdin = open('input.txt','r')

N = int(input())
List = []

for _ in range(N):
    start, stop = map(int, input().split())
    List.append([start, stop])

# 시작 시간을 기준으로 정렬
List.sort()

room = []  # 강의실 종료 시간을 저장하는 우선순위 큐

for i in range(N):
    if not room or room[0] > List[i][0]:
        # 현재 수업의 시작 시간이 이전 수업의 끝나는 시간보다 빠르면 새로운 강의실 필요
        heapq.heappush(room, List[i][1])
    else:
        # 현재 수업의 시작 시간이 이전 수업의 끝나는 시간보다 늦으면 강의실 재활용 가능
        heapq.heappop(room)
        heapq.heappush(room, List[i][1])

print(len(room))
