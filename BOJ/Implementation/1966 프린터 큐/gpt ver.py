import sys

sys.stdin = open('input.txt', 'r')

TC = int(input())

for _ in range(TC):
    N, M = map(int, input().split())
    Priority = list(map(int, input().split()))
    target = M  #인덱스로 이용
    count = 0

    while True:
        if Priority[0] == max(Priority):
            if target == 0:  # target 인덱스가 0이라면 끝
                count += 1
                print(count)
                break
            else:
                Priority.pop(0)
                N -= 1
                target = (target - 1 + N) % N
                count += 1
        elif Priority[0] != max(Priority):
            temp = Priority[0]
            Priority.append(temp)
            Priority.pop(0)
            target = (target - 1 + N) % N  # Update the target index after rotation
