import sys
sys.stdin = open('input.txt', 'r')

Data = [list(map(int, input().split())) for i in range(5)]

for y in range(5):
    for x in range(5):
        print(Data[y][x],end ='')
    print()

for x in range(5):
    for y in range(5):
        print(Data[y][x],end ='')
    print()