import sys
sys.stdin = open('input.txt', 'r')

T = input()
for i in range(len(T)):
    if i == len(T) - 1:  # 마지막 인덱스일 때는 띄어쓰기 없이 출력
        print(i + 1, end="")
    else:
        print(i + 1, end=" ")