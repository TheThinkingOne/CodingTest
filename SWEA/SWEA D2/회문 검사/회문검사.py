# import sys
# sys.stdin = open('input.txt','r')
#
# T = int(input())
# for i in range(T):
#     Data = list(map(str,input()))
#     CheckPalindrome1 = ''
#     CheckPalindrome2 = ''
#     Result = 0
#     for j in range(len(Data)//2):
#         for k in range(len(Data)//2-1,-1,-1):
#             CheckPalindrome1 += Data[j]
#             CheckPalindrome2 += Data[k]
#             if CheckPalindrome1 == CheckPalindrome2:
#                 Result = 1
#             else:
#                 Result = 0
#     print(f"{i+1} {Result}")

import sys
sys.stdin = open('input.txt','r')

T = int(input())
for i in range(T):
    Data = list(map(str,input()))
    CheckPalindrome1 = ''
    CheckPalindrome2 = ''
    Result = 0
    for j in range(len(Data)//2):
        CheckPalindrome1 += Data[j]
        CheckPalindrome2 += Data[-1-j]
        if CheckPalindrome1 == CheckPalindrome2[::-1]:
            Result = 1
        else:
            Result = 0
    print(f"{i+1} {Result}")


