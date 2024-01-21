import sys

sys.stdin = open('input.txt', 'r')

howmany = int(input())

for tc in range(howmany):
    Data = list(map(int, input().split()))

    # 최대값과 최소값의 위치를 찾습니다.
    max_index = Data.index(max(Data))
    min_index = Data.index(min(Data))

    # 최대값과 최소값의 위치를 바꿉니다.
    Data[max_index], Data[min_index] = Data[min_index], Data[max_index]

    print(f"#{tc + 1}", " ".join(map(str, Data)))










