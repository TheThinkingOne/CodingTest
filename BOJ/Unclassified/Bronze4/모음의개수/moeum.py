import sys

sys.stdin = open('input.txt', 'r')

results = []  # 각 줄의 모음 수를 저장할 리스트

for i in range(3):
    sum = 0
    Data = input().strip()  # 공백 제거
    for char in Data:
        if char in 'AEIOUaeiou':
            sum += 1
    results.append(sum)

print(' '.join(map(str, results)))  # 각 줄의 모음 수 출력




