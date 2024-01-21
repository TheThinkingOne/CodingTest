import sys
sys.stdin = open('input.txt', 'r')

for i in range(4):
    TC = int(input())
    nums = list(map(int,input()))
    total = 0
    for k in range(len(nums)):
        total += nums[k]
    print(total)

