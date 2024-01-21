import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
A = list(map(int,input().split()))
B, C = map(int,input().split())
countList = []
#B: 총감독관이 한 시험장에서 감시할 수 있는 응시자의 수
#C: 부감독관이 한 시험장에서 감시할 수 있는 응시자의 수

for i in range(len(A)):
    count = 0
    if A[i] <= B:
        count += 1
        countList.append(count)
    elif A[i] > B:
        A[i] -= B
        count += 1
        while A[i] >= 0:
            A[i] -= C
            count += 1
        countList.append(count)
print(sum(countList))


