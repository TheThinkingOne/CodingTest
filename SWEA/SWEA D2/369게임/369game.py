import sys
sys.stdin = open('input.txt','r')

T = int(input())
s= []

for i in range(1,T+1):
    s.append(str(i))

for nums in s:
    count = 0
    for j in nums:
        if j in '369':
            count+=1
    if count == 0:
        print(nums,end=' ')
    else:
        print('-' * count, end = ' ')

