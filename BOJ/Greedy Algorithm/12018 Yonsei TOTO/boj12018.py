import sys
sys.stdin = open('input.txt','r')

mileageList = []
count = 0

N, M = map(int,input().split())
for i in range(N):
    P, L = map(int,input().split())
    #P: 신청한 사람 수, L: 수강인원
    mileage = list(map(int,input().split()))

    if P < L:
        required = 1
        mileageList.append(required)
    elif P == L:
        required = min(mileage)
        mileageList.append(required)
    elif P > L:
        mileage.sort()
        if min(mileage) == 36:
            required = 36
            mileageList.append(required)
        else:
            required = mileage[P - L]
            mileageList.append(required)

mileageList.sort()
#print(mileageList)
for i in range(len(mileageList)):
    M -= mileageList[i]
    if M < 0: break
    count += 1
print(count)






