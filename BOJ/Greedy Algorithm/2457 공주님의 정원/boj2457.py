import sys
sys.stdin = open('input.txt','r')

N = int(input())

all_plus = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
               #1  #2  #3   4    5    6    7    8    9    10   11   12
March1st_to_Nov30th = 273

def daySum(mon1, day1, mon2, day2):
    if mon1 == mon2:
        daysum = day2 - day1 + 1
    elif mon2 > mon1:
        daysum = (all_plus[mon2-1] + day2) - (all_plus[mon1-1]+day1) +1
    elif mon1 > mon2:
        daysum = 365 - (all_plus[mon1-1]+day1) + (all_plus[mon2-1] + day2) + 1

    return daysum

for i in range(N):
    #fullBloom = list(map(int,input().split()))
    mon1, day1, mon2, day2 = map(int,input().split())



    # if mon2 == 12 and

