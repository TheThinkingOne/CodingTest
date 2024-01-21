import sys
sys.stdin = open('input.txt','r')

T = int(input())
for i in range(T):
    N = int(input())
    nums = list(map(int,input().split()))
    for k in range(N):
        if nums[k] <= nums[k+1]:
