import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for i in range(T):
    nums = list(map(int, input().split()))
    average = round(sum(nums) / len(nums))
    print(f"#{i+1} {average}")
