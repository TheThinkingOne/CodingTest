import sys
sys.stdin = open('input.txt','r')

N = int(input())
scoreList = []
count = 0

for _ in range(N):
    score = int(input())
    scoreList.append(score)

for i in range(N-1):
    while scoreList[i] >= scoreList[i+1]:
    #앞 점수가 뒷 점수보다 크거나 같은 동안
        scoreList[i] -= 1
        count += 1
        # if i != 0 and scoreList[i-1] == scoreList[i]:
        #     count += 1
        # elif scoreList[i] == scoreList[i+1]:
        #     count += 1

print(count)

# def adjustingScore():
#     global count
#     while scoreList[i] >= scoreList[i+1]:
#     #앞 점수가 뒷 점수보다 크거나 같은 동안
#         scoreList[i] -= 1
#         count += 1