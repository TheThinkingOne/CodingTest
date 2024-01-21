import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
#B: 총감독관이 한 시험장에서 감시할 수 있는 응시자의 수
#C: 부감독관이 한 시험장에서 감시할 수 있는 응시자의 수

Supervisors = 0

for i in range(N):
    Supervisors += 1

    # 부감독관 필요 수 계산
    if A[i] > B:  # 총감독관만으로 감시가 불가능한 경우
        remain = A[i] - B  #남은 시험응시자 수
        if remain % C == 0: #부감독관 감시 가능 수 만큼 나눠떨어지는 경우
            Supervisors += remain // C #나눈 수 만큼 필요감독관 더하기
        else:
            Supervisors += remain // C + 1 #한명 더 필요인원 ++

print(Supervisors)
