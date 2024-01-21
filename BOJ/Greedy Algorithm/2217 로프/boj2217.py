import sys
sys.stdin = open('input.txt','r')

N = int(input())
ropeList = []
ropeSum = []
WList = []

for _ in range(N):
    rope = int(input())
    ropeList.append(rope)

#당연히 가장 튼튼한 로프부터 들어올리겠지?

for i in range(N-1,-1,-1):
    ropeSum.append(ropeList[i])
    W = int(min(ropeSum) * len(ropeSum))
    WList.append(W)

print(WList)
print(max(WList))



