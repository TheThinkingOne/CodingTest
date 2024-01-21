import sys

for i in range(4):
    TC = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline()))
    total = 0
    for k in range(len(nums)):
        total += nums[k]
    print(total)