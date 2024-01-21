import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
List = []
Room = []

for _ in range(N):
    start, stop = map(int, input().split())
    List.append([start, stop])

# 시작 시간을 기준으로 정렬
List.sort()
Room.append(List[0][1])  # 첫 번째 수업이 끝나는 시간을 초기값으로 설정

for i in range(1, N):
    if List[i][0] < Room[0]:
        # 현재 수업의 시작 시간이 이전 수업의 끝나는 시간보다 빠르면 새로운 강의실 필요
        Room.append(List[i][1])
    else:
        Room.pop(0)
        Room.append(List[i][1])

print(len(Room))
