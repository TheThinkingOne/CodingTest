import sys
sys.stdin = open('input.txt','r')

N = int(sys.stdin.readline())
Nset = set(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
Mset = set(map(int,sys.stdin.readline().split()))

for i in Mset:
    if i in Nset:
        print(1, end=" ")
    else:
        print(0, end=" ")

#Set형(집합형)을 이용한 시간 복잡도 최적화
#Set형은 키와 값을 저장하는 방식을 이용해 상수 시간에 검색이 가능함