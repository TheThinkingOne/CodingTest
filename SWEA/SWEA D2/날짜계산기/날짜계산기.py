import sys
sys.stdin = open('input.txt','r')

all_plus = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
               #1  #2  #3   4    5    6    7    8    9    10   11   12

T = int(input())
for i in range(T):
    mon1, day1, mon2, day2 = map(int,input().split())
    daysum = 0
    if mon1 == mon2:
        daysum = day2 - day1 + 1
    elif mon2 > mon1:
        daysum = (all_plus[mon2-1] + day2) - (all_plus[mon1-1]+day1) +1
    elif mon1 > mon2:
        daysum = 365 - (all_plus[mon1-1]+day1) + (all_plus[mon2-1] + day2) + 1
    print(f"#{i+1} {daysum}")





    # if mon1 == mon2:
    #     Days = day2 - day1 + 1
    # elif mon1 != mon2:
    #     if mon1 > mon2:
    #
    # elif mon2 > mon1:




    #     if mon1 == '2':
    #         Days = (28-day1) + day2 + 1
    #     elif mon1 in '1,3,5,7,8,10,12':
    #         Days = (31-day1) + day2 + 1
    #     else:
    #         Days = (30-day1) + day2 + 1
