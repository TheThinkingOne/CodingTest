import sys
sys.stdin = open('input.txt','r')

N = int(input())
scoreList = []

for _ in range(N):
    score = int(input())
    scoreList.append(score)

count = 0
for i in range(N - 1, 0, -1):  # 뒤에서부터 앞으로 확인
    if scoreList[i] <= scoreList[i - 1]:  # 현재 레벨보다 앞 레벨의 점수가 더 크거나 같다면
        count += (scoreList[i - 1] - scoreList[i] + 1)  # 현재 레벨을 조정하여 앞 레벨과 같게 만들기 위한 조정 횟수를 더합니다
        scoreList[i - 1] = scoreList[i] - 1  # 앞 레벨을 현재 레벨 - 1로 만듭니다

print(count)
