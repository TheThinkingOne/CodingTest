import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

candidates = []

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i != j and j != k and k != i:
                candidates.append((str(i), str(j), str(k)))
                #숫자 비교를 위해 각각 String으로 저장

for _ in range(N):
    n, s, b = map(int, input().split())
    #n은 서로 다른 숫자로 이루어진 3자리 숫자
    n = list(str(n))
    #print(n)
    temp_candidates = []

    for num in candidates:
        strike = ball = 0 #각각의 리스트에 대해 스트라이크, 볼 초기화
        for j in range(3):
            if num[j] == n[j]:
                strike += 1
            elif num[j] in n:
                ball += 1

        if strike == s and ball == b:
            temp_candidates.append(num)

    candidates = temp_candidates
    #연산이 진행됨에 따라 새로운 리스트가 업데이트 됨, 경우의 수가 줄어듦

print(len(candidates)) #최종 답 출력
