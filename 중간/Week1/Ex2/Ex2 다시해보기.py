import sys
sys.stdin = open('input.txt', 'r')

Data = list(map(int, input().split()))

Max = Data[0]

for tc in range(len(Data)):
    if Data[tc] == max(Data):
        wheremax = tc
        print(f"최대값은 {Data[tc]}")
        print(f"그 위치는 {tc}")

