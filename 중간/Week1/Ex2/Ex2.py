import sys
sys.stdin = open('input.txt', 'r')

Data = list(map(int, input().split()))

max = Data[0]
wheremax = 0

for i in range(len(Data)):
    if Data[i] > max:
        max = Data[i]
        wheremax = i

print(f"#최대값은 : {max}")
print(f"최대값의 위치는 : {wheremax}")