import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(T):
    plusNum = 0
    nums = list(map(int, input().split()))
    for i in range(len(nums)):
        if nums[i] % 2 == 1:
            plusNum += nums[i]
    print(f"#{tc+1} {plusNum}")
