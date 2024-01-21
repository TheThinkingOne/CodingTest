import sys
sys.stdin = open('input.txt','r')

S = input()
List = [int(char) for char in S]
#print(List)
Act = 0

if sum(List) == len(List) or sum(S) == 0:
    print(Act)
else:
    for i in range(len(List)):
        if sum(List) >= len(list) / 2:
            


